"""Demonstration harness for converting a mocked trade into BGL XML output.

The dictionary below mirrors the fields produced by custodians/brokers and is
kept deliberately explicit so newcomers can see how each key feeds into the
``bgl_xml`` transformation pipeline.
"""

from bgl_xml import bgl_xml

trade_transaction={}
# A trade exported from a broker will identify itself as a ``Trade`` event.
trade_transaction['Transaction_Type']="Trade"
# Dates are provided in DD/MM/YYYY format as expected by BGL.
trade_transaction['Transaction_Date']='12/05/2025'
trade_transaction['Amount']='6043.43'
trade_transaction['Currency']='USD'
# Narrative exactly as captured on the contract note, used for audit trails.
trade_transaction['Description']= (
    'BUY 3476.0000 SHARES OF PLX @ 1.73000ISIN# US74365A3095 '
    '(PROTALIX BIOTHERAPEUTICS INC COM NEW UNSOLICITED ORDER)'
)
# Broker exports often include both a security type and security code.
trade_transaction['Security_Type']='Shares in Listed Companies (Overseas)'
trade_transaction['Quantity']='PLX.AME'
trade_transaction['Security_Code']='PLX.AME'
trade_transaction['Quantity']='3476'
trade_transaction['Brokerage']='29.95'
trade_transaction['Settlement_Date']= '13/05/2025'
trade_transaction['Contract_Date']='3476'
trade_transaction['Transaction_ID']='IV250512PLXbuy85'

history_transactions=[trade_transaction]
# Feed the mocked transaction into the converter so new developers can inspect
# the generated ``BGL.xml`` file and understand how the XML structure is built.
bgl_xml(history_transactions)
