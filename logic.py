import json

managers_list = {}
watchers_list = {}

def parse_json():
  with open('source_file_2.json', 'r') as f:
    projects = json.loads(f.read())
    projects.sort(key=lambda x: x['priority'], reverse=True)
    for item in projects:
      for manager in item['managers']:
        if manager not in managers_list:
          managers_list[manager] = []
        managers_list[manager].append(item['name'])
      for watcher in item['watchers']:
        if watcher not in watchers_list:
          watchers_list[watcher] = []
        watchers_list[watcher].append(item['name'])

def create_json_file():
  with open('managers.json', 'w+') as managers_json:
    json.dump(managers_list, managers_json)
  with open('watchers.json', 'w+') as watchers_json:
    json.dump(watchers_list, watchers_json)

parse_json()
create_json_file()
