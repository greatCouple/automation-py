from ProjectPath import work_path
import yaml, os


class YamlUtil:
    @staticmethod
    def read(fileName):
        file = work_path + "/config/" + fileName + '.yaml'
        print(file)
        if os.path.exists(file):
            pass
        else:
            raise FileNotFoundError('配置文件不存在')
        with open(file, 'rb') as f:
            return yaml.safe_load(f)


if __name__ == '__main__':
    YamlUtil.read('driverConfig')
