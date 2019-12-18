from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('Qd7Yoxda8bbT/7MszbABx0ML+Y2qx52cTPWdX80D9VbBZC7V/kXZDbBS8UUNN35yTu+4TFM6bopguF7W632kKejTTrS301YXUqnShnJDUcYxxCJEe6FceN0WvdVEjgQFXPmVyIKhY/ik9cJxfxvaDQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e618d5e7fa1816a89794183a80b7700f')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    re = "超過回覆範圍喔! 麻煩重新再輸入一次"

    if "貼圖" in msg:
        sticker_message = StickerSendMessage(
            package_id = "11537" ,
            sticker_id = "52002744"
            )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    if "我要預訂" in msg:
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(thumbnail_image_url='https://scontent.ftpe8-2.fna.fbcdn.net/v/t1.0-9/78858712_3020675774617584_8482206259481673728_n.jpg?_nc_cat=103&_nc_ohc=LcqCtsc9Mg4AQkWAfO3bHQkSFkQehfvv6JcB8Uph07V7mgieZ6G3k749w&_nc_ht=scontent.ftpe8-2.fna&oh=d0720b979ae3ae5e8164f4c3f7bcb2b1&oe=5E7D327A',
                           text='請填寫表單，完成後來電確認到貨日期，取貨時付款即可\nTime : 09:00-21:00\nTEL : 0905-675038', title='台中高鐵站門市(自取)',
                           actions=[
                URIAction(label='訂購表單', uri='https://bit.ly/2Lhgrnx'),
                MessageAction(label='門市地址', text='高鐵門市地址')
            ]),
            CarouselColumn(thumbnail_image_url='https://scontent.ftpe8-2.fna.fbcdn.net/v/t1.0-9/79327003_3020675734617588_111192146333138944_n.jpg?_nc_cat=103&_nc_ohc=TtWIs9eKc-sAQmpge1FFJnBDoRemxWS3a0-LVR6sHLhT35_mS8IKxTsXg&_nc_ht=scontent.ftpe8-2.fna&oh=27b81efab9bcbdf4f8d92525515d998b&oe=5EB39E9E',
                           text='請填寫表單，完成後來電確認到貨日期，取貨時付款即可\nTime : 09:00-21:00\nTEL : 0905-675038', title='美村門市(自取)',
                           actions=[
                URIAction(label='訂購表單', uri='https://bit.ly/2sAgS4I'),
                MessageAction(label='門市地址', text='美村本店地址')
            ]),
            CarouselColumn(thumbnail_image_url='https://scontent.ftpe8-2.fna.fbcdn.net/v/t1.0-9/78918939_3020675737950921_6237532466555387904_n.jpg?_nc_cat=103&_nc_ohc=uxxSk9XOLYUAQmc7lzkDRhNhk_h3LuzTRyKHIboEsX2zHsU8rSeqA6H0g&_nc_ht=scontent.ftpe8-2.fna&oh=015d9b93ba1d4b91c68abba29933dca0&oe=5E7DC110',
                           text='全台冷凍宅配，請先來電確到貨日期及數量，填寫完訂單後再行匯款 或 貨到付款', title='宅配預訂',
                           actions=[
                URIAction(label='訂購表單', uri='https://bit.ly/2sAgS4I'),
                MessageAction(label='合作宅配廠商', text='合作宅配廠商')
            ])
        ])
        template_message = TemplateSendMessage(
            alt_text='Carousel alt text', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return

    if "產品資訊" in msg:
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
            original_content_url='https://scontent.ftpe8-3.fna.fbcdn.net/v/t1.0-9/s960x960/79166425_3020749467943548_6137808969529294848_o.jpg?_nc_cat=111&_nc_ohc=CJAdUCHDtGsAQmInLfUa2pXq9GluGs5NkFKBj9m-aD5k4U5lv_XChYHLA&_nc_ht=scontent.ftpe8-3.fna&oh=8b796562847de0afb92814b3ab161e45&oe=5E855925', preview_image_url='https://scontent.ftpe8-3.fna.fbcdn.net/v/t1.0-9/s960x960/79166425_3020749467943548_6137808969529294848_o.jpg?_nc_cat=111&_nc_ohc=CJAdUCHDtGsAQmInLfUa2pXq9GluGs5NkFKBj9m-aD5k4U5lv_XChYHLA&_nc_ht=scontent.ftpe8-3.fna&oh=8b796562847de0afb92814b3ab161e45&oe=5E855925')
                                   )
        return

    if "疑問?" in msg:
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://scontent.ftpe8-1.fna.fbcdn.net/v/t1.0-9/79700129_3028430623842099_7126640471203381248_n.jpg?_nc_cat=105&_nc_ohc=EVvK1FJ1Hx0AQkYVs6ZndjKBRxnCe4kkCqozIAoPsgbYC-F1KyP5-9ycA&_nc_ht=scontent.ftpe8-1.fna&oh=a19374d1a71bffe76e0befb5470eacec&oe=5E70FB25',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='https://scontent.ftpe8-1.fna.fbcdn.net/v/t1.0-9/79700129_3028430623842099_7126640471203381248_n.jpg?_nc_cat=105&_nc_ohc=EVvK1FJ1Hx0AQkYVs6ZndjKBRxnCe4kkCqozIAoPsgbYC-F1KyP5-9ycA&_nc_ht=scontent.ftpe8-1.fna&oh=a19374d1a71bffe76e0befb5470eacec&oe=5E70FB25', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='常見問題', weight='bold', size='xl')
                        ]
                    ),
                
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # callAction, separator, websiteAction
                    SpacerComponent(size='sm'),
                    # callAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label='最佳食用方式?', text="最佳食用方式?"),
                    ),
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label='建議搭配飲品?', text="建議搭配飲品?")
                    ),
                    SeparatorComponent(),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label='素食者可以吃嗎?', text="素食者可以吃嗎?")
                    ),
                    SeparatorComponent(),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label='運費計算方式?', text="運費計算方式?")
                    ),
                    SeparatorComponent(),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label='宅配可以貨到付款嗎?貨到付款需要另外支付手續費?', text="宅配可以貨到付款嗎?貨到付款需要另外支付手續費?")
                    ),
                    SeparatorComponent(),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label='一般訂購跟彌月訂購價格一樣嗎?', text="一般訂購跟彌月訂購價格一樣嗎?")
                    ),
                    SeparatorComponent(),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label='保冷劑跟保冷袋需要加購嗎?', text="保冷劑跟保冷袋需要加購嗎?")
                    ),
                    SeparatorComponent(),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label='有團購優惠嗎?', text="有團購優惠嗎?")
                    ),
                    SeparatorComponent(),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label='可以告訴我完整的訂購流程嗎?', text="可以告訴我完整的訂購流程嗎?")
                    ),
                    SeparatorComponent(),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=MessageAction(label='期待新的產品推出', text="期待新的產品推出")
                    )
                ]
            ) 
        )
        message = FlexSendMessage(alt_text="花鳥川水果千層蛋糕", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
        return

    if "高鐵門市地址" in msg:
        re = "台中高鐵站內摩斯漢堡對面"
    elif "美村本店地址" in msg:
        re = "台中市西區美村路一段596巷14號"
    elif "最佳食用方式?" in msg:
        re = "怎麼吃都好吃!但從冷凍取出後可以先常溫放5分鐘軟化會比較好切"
    elif "運費計算方式?" in msg:
        re = "宅配皆為冷凍宅配喔!\n1-2條/箱 : 160元\n3-8條/箱 : 225元\n9-11條 : 290元\n12-20條/箱 : 免運費!"
    elif "建議搭配飲品?" in msg:
        re = "紅茶(?...啊我不知道啦"
    elif "素食者可以吃嗎?" in msg:
        re = "本產品為奶蛋素喔 !"
    elif "期待新的產品推出" in msg:
        re = "非常感謝您的支持! 目前只有檸檬千層蛋糕喔~我們也正在努力研發新口味~敬請期待!!!"
    elif "一般訂購跟彌月訂購價格一樣嗎?" in msg:
        re = "這個目前不清楚，等老闆娘回國會再回覆您XD"
    elif "保冷劑跟保冷袋需要加購嗎?" in msg:
        re = "凡購買產品，每條皆附保冷劑一個以及鋁箔包裝(夏日保冷3小時，秋冬保冷4小時)。\n加購的部分: 1個保冷劑10元、2個保冷劑20元"
    elif "可以告訴我完整的訂購流程嗎?" in msg:
        re = "目前的訂購流程為:\nStep1. 先來電確認欲宅配日期及數量\nStep2. 訂購表單\nStep3. 填寫完後煩請再次來電或粉絲團留言，確認訂單成立\n日後訂購方式或流程如有變化會再通知大家的~感謝您!"
    elif "有團購優惠嗎?" in msg:
        re = "有的! 凡團購20條(或20條的倍數)，不但免運費，每條價格降為380元喔!"
    elif "宅配可以貨到付款嗎?貨到付款需要另外支付手續費?" in msg:
        re = "宅配可以選擇貨到付款喔!\n手續費的部分:\n貨款2000以下，手續費30元\n貨款總額2001-5000元，手續費60元\n貨款總額5001-10000元，手續費90元"
    elif "合作宅配廠商" in msg:
        re = "黑貓宅急便"
    

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=re))


if __name__ == "__main__":
    app.run()
