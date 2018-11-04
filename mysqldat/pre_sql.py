'''
   @Author Ci Xin
   @E-mail sssrrr879@126.com
   @Phone 15849311404
   @Desc 存放pre_SQL语句
   @Date Create on 2018/11/4/004 20:24
'''

sql = {
    'c_dytt_movies': "INSERT INTO `moviespider`.`dytt_movies` (`mhome`, `classic`,`mname`, `mdesc`, `mtime`, `hot`, `makedate`, `maketime`, `modifydate`, `modifytime`)VALUES('{0}','{1}','{2}','{3}','{4}','{5}'+0,'{6}','{7}','{8}','{9}');",
    'c_dytt_download': "INSERT INTO `moviespider`.`dytt_download` ( `mid`,`downloadurl`,`makedate`,`maketime`,`modifydate`,`modifytime`)VALUES('{0}'+0,'{1}','{2}','{3}','{4}','{5}');",
    's_dytt_movies_lastid': 'SELECT DISTINCT LAST_INSERT_ID() FROM `moviespider`.`dytt_movies`;',
    's_dytt_download_lastid': 'SELECT DISTINCT LAST_INSERT_ID() FROM `moviespider`.`dytt_download`;',
    's_dytt_movies_exits': "SELECT COUNT(1) FROM `moviespider`.`dytt_movies` WHERE mname = '{0}' ",
    'c_dytt_log': "INSERT INTO `moviespider`.`dytt_log` (`home`, `errorsql`,`errorinfo`, `datetime`) VALUES ('{0}', '{1}', '{2}','{3}');",

}
