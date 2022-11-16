from IIFLapis import IIFLClient

client = IIFLClient(client_code="56839266", passwd="Heyiifl@4", dob="19990904", email_id="ravikumaresh7766@gmail.com",contact_number="8667810144")
client.client_login() #For Customer Login

#NOTE : Symbol has to be in the same format as specified in the example below.

req_list_=[{"Exch":"N","ExchType":"C","ScripCode":"22"},
            {"Exch":"N","ExchType":"C","ScripCode":"5258"}]

client.fetch_market_feed(req_list=req_list_, count=2,client_id="56839266")

###5258 = industindbank
#To fetch historical candle data, jwt token needs to be validated first.
client.jwt_validation("56839266")

#After successful jwt validation, historical data can be fetched.            
client.historical_candles(exch='n',exchType='c',scripcode='5258',interval='5m',fromdate='2022-11-01',todate='2022-11-30',client_id="56839266")

# Fetches client profile
client.profile(client_id = "56839266")

# Fetches holdings
client.holdings(client_id = "56839266")

# Fetches DP holdings
client.dp_holdings(client_id = "56839266")

# Fetches margin
client.margin(client_id = "56839266")

# Fetches net positions
client.net_positions(client_id = "56839266")

# Fetches net wise positions
client.net_position_netwise(client_id = "56839266")

# Fetches the order book of the client
client.order_book(client_id = "56839266")

# Fetches the trade book of the client
client.trade_book(client_id = "56839266")

from IIFLapis.order import Order, OrderType, Exchange, ExchangeSegment, OrderValidity, AHPlaced

test_order = Order(order_type="BUY", scrip_code=5258, quantity=1, exchange="N",
    exchange_segment="C", price=555, is_intraday=False, atmarket=False, order_id=2,
    remote_order_id="1", exch_order_id="0", DisQty=0, stoploss_price=0,
    is_stoploss_order=False, ioc_order= False, is_vtd=False,ahplaced = AHPlaced.AFTER_MARKET_CLOSED,
    public_ip='192.168.1.1', order_validity=OrderValidity.DAY, traded_qty=0)
client.place_order(order=test_order,client_id='56839266',order_requester_code='56839266')


#Short Straddle
client.short_straddle(symbol='BANKNIFTY',expiry='24 Nov 2022',strike_price='42000',qty='75',isIntra=True,client_id='56839266',order_requester_code='56839266',RemoteOrderID='XYZ010101')

