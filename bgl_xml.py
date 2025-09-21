import xml.etree.ElementTree as ET

sp="    "


def new_transaction(root,dic,end_row=False):
    transactions = root.find(".//Transactions")
    element=ET.SubElement(transactions,"Transaction")
    element.text="\n"+sp+sp+sp+sp
    if end_row==True:
        element.tail="\n"+sp+sp
    else:
        element.tail="\n"+sp+sp+sp   
    len_dic=len(dic)
    k=0
    for key in dic.keys():
        print(key, dic[key])
        #transaction_sub_element(root,key,transaction[key])
        sub_element=ET.SubElement(element,key)
        sub_element.text=dic[key]
        if k==len_dic-1:
            sub_element.tail="\n"+sp+sp+sp
        else:
            sub_element.tail="\n"+sp+sp+sp+sp
        k=k+1
    return root

def ticker_bgl_format(security_code,exchange=None):
    if "." in security_code:
        ticker=security_code.split(".")[0]
        if exchange is None:
            exchange=security_code.split(".")[1]        
    if ticker=="PER783RR7":
        return ticker
    if ticker=="GAZP":
        return "GAZP.MOEX"
    if ticker=="LKOH":
        return "LKOH.MOEX"
    if ticker=="SIL":
        return "SIL.ARCX"
    if ticker =="FBMS":
        return "FBMS.NDQ"
    if ticker == "JUVF":
        return "JUVF.OTC"
    #if exchange is None:
        #exchange=stock.exchange(ticker)
    #if exchange=="Ticker Not Found":
        #exchange=stock.wbc_exchange(ticker)
    if exchange=="NASDAQ" or exchange=="NASD"  :
        new_ticker=ticker+"."+"NDQ"
    elif exchange=="NYSE" or "NYE":
        new_ticker=ticker+"."+"NYE"
    elif exchange=="AMER" or exchange=="AMEX" or exchange=="NYSEAMER"  :
        new_ticker=ticker+"."+"AME"
    elif exchange[0:3]=="OTC":
        new_ticker=ticker+"."+"OTC"
    else:
        print("stock xchange not found")
        print(i, ticker, exchange)
        raise SystemExit(0)
    return new_ticker

def trade(root,stock_transaction,with_bank,end_row):
    investment={}
    investment["Transaction_Type"]="Investment Transaction"
    investment["Transaction_Date"]=stock_transaction["Transaction_Date"]
    investment["Description"]=stock_transaction["Description"]
    investment["Amount"]=str(abs(float(stock_transaction["Amount"])))
    if "sell" in investment["Description"].lower():
        investment["Amount"]="-"+investment["Amount"]
    investment["Currency"]=stock_transaction["Currency"]    
    if investment["Currency"]=="USD":
        investment["Security_Type"]="Shares in Listed Companies (Overseas)"
    if "Exchange" in stock_transaction.keys():
        investment["Security_Code"]=ticker_bgl_format(stock_transaction["Security_Code"],stock_transaction["Exchange"])
    else:
        investment["Security_Code"]=ticker_bgl_format(stock_transaction["Security_Code"])
    investment["Quantity"]=stock_transaction["Quantity"]
    investment["Brokerage"]=stock_transaction["Brokerage"]
    investment["Settlement_Date"]=stock_transaction["Settlement_Date"]
    investment["Contract_Date"]=investment["Transaction_Date"]
    investment["Transaction_ID"]="IV"+stock_transaction["Transaction_ID"]
    if with_bank==True:
        bank={}
        bank["Transaction_Type"]="Bank Transaction"
        bank["Amount"]="-"+investment["Amount"]
        bank["Currency"]=investment["Currency"]
        bank["Transaction_Date"]=investment["Settlement_Date"]
        bank["Transaction_ID"]="BK"+stock_transaction["Transaction_ID"]
    print(investment)
    new_transaction(root,bank)
    if end_row==True:
        new_transaction(root,investment,True)
    else:
        new_transaction(root,investment)
    #print("before return")
    return root

def bgl_xml(history_transactions):
#for cc in range(0,1):
    tree=ET.ElementTree()
    root=ET.Element("BGL_Import_Export")
    root.text="\n"+sp
    supplier=ET.Element("Supplier")
    supplier.text="BGL"
    supplier.tail="\n"+sp
    root.append(supplier)
    product=ET.Element("Product")
    product.text="SF360"
    product.tail="\n"+sp
    root.append(product)
    version=ET.Element("Version")    
    version.text="1.2"
    version.tail="\n"+sp
    root.append(version)
    entity_details=ET.Element("Entity_Details")    
    entity_details.text="\n"+sp+sp
    entity_details.tail="\n"
    root.append(entity_details)
    entity_code=ET.SubElement(entity_details,"Entity_Code")
    entity_code.text="BGL"
    entity_code.tail="\n"+sp+sp
    transactions=ET.SubElement(entity_details,"Transactions")
    transactions.text="\n"+sp+sp+sp
    transactions.tail="\n"+sp

    for history_transaction in history_transactions:
        if history_transaction["Transaction_Type"]=="Trade":
            trade(root,history_transaction,True,True)

    tree._setroot(root)
    print("Begin Output")
    output=ET.tostring(root,encoding="ISO-8859-1")
    with open("BGL.xml", "wb") as f:
    #with open("F:/GFG.xml", "wb") as f:
        f.write(output)
    print("end output")

