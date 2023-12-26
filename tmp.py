def convert_ip_to_bin(ipaddr):
    a,b,c,d = ipaddr.split('.')
    a,b,c,d = int(a), int(b),int(c), int(d)
    res = ""
    lst = [a,b,c,d]
    for num in lst:
        tres = ""
        while num !=0:
            rem = num%2
            tres = str(rem)+tres
            num = num//2
        #prepend with zeros
        prep = 8-len(tres)
        res = res+ ("0"*prep+tres)
    return res

def convert_ip_to_binary(ipaddr):
    lst =  map(int,ipaddr.split('.'))
    binrep = [ bin(ele)[2:] for ele in lst]
    print("binrep ",  binrep)



# def output(src_ip, dest_ip, acl_src, acl_dest):
#     src_subnet, dest_subnet = int(acl_src.split('/')[1]), int(acl_dest.split('/')[1])
#     dec_ips = [src_ip, dest_ip, acl_src.split('/')[0], acl_dest.split('/')[0]]
#     bin_ips = []
#     for i in range(4):
#         bin_ips.append(convert_ip_to_bin(dec_ips[i]))
    
#     if bin_ips[0][: src_subnet+1] != bin_ips[2][: src_subnet+1]:
#         return False
    
#     if bin_ips[1][: dest_subnet+1] != bin_ips[3][: dest_subnet+1]:
#         return False
    
#     return True
    
    
    


if __name__ == "__main__":
    src_ip, dest_ip = input().split()
    # acl_src, acl_dest = input().split() #space
    # print(output(src_ip, dest_ip, acl_src, acl_dest))
    convert_ip_to_binary(dest_ip)
    