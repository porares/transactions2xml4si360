from bgl_xml import bgl_xml

trade_transaction={}
trade_transaction['Transaction_Type']="Trade"
trade_transaction['Transaction_Date']='12/05/2025'
trade_transaction['Amount']='6043.43'
trade_transaction['Currency']='USD'
trade_transaction['Description']= 'BUY 3476.0000 SHARES OF PLX @ 1.73000ISIN# US74365A3095 (PROTALIX BIOTHERAPEUTICS INC COM NEW UNSOLICITED ORDER)'
trade_transaction['Security_Type']='Shares in Listed Companies (Overseas)'
trade_transaction['Quantity']='PLX.AME'
trade_transaction['Security_Code']='PLX.AME'
trade_transaction['Quantity']='3476'
trade_transaction['Brokerage']='29.95'
trade_transaction['Settlement_Date']= '13/05/2025'
trade_transaction['Contract_Date']='3476'
trade_transaction['Transaction_ID']='IV250512PLXbuy85'

history_transactions=[trade_transaction]
bgl_xml(history_transactions)
