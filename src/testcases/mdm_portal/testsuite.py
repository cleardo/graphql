if __name__ == '__main__':
    import os
    # 实例化测试套件对象
    s = unittest.TestSuite()
    # 实例化TestLoader的对象
    loader = unittest.TestLoader()
    # 使用discover()去找一个目录下的所有测试用例的文件,并将返回数据添加到测试套件中。
    s.addTests(loader.discover(os.getcwd()))
    run = unittest.TextTestRunner()
    run.run(s)
