from src.utils.ProjectPath import Path
import yaml, os


class ReadYaml:
    def __init__(self):
        self.yamlPath = Path().work_path + "/config/"

    def readYaml(self, fileName):
        file = self.yamlPath + fileName + '.yaml'
        if os.path.exists(file):
            pass
        else:
            raise FileNotFoundError('配置文件不存在')
        with open(file, 'rb') as f:
            return yaml.safe_load(f)


if __name__ == '__main__':
    ReadYaml().readYaml('trainer')


