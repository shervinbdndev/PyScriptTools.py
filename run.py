from PyScriptTools import NetworkTools , OtherTools


if __name__ == "__main__":
    network_object = NetworkTools()
    use_ascii = OtherTools()
    print(use_ascii.ConvertToAscii(network_object.ShowLocalIP() , ["green" , "red"] , "left" , "shade"))

    """ Enjoy All Methods And Use Them EveryWhere ! ! ! """
    """ Author's Github : https://github.com/shervinbdndev """
