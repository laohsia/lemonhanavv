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
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://scontent.ftpe8-2.fna.fbcdn.net/v/t1.0-9/78858712_3020675774617584_8482206259481673728_n.jpg?_nc_cat=103&_nc_ohc=LcqCtsc9Mg4AQkWAfO3bHQkSFkQehfvv6JcB8Uph07V7mgieZ6G3k749w&_nc_ht=scontent.ftpe8-2.fna&oh=d0720b979ae3ae5e8164f4c3f7bcb2b1&oe=5E7D327A',
                title='台中高鐵站門市(自取)',
                text='請填寫表單，完成後來電確認，取貨時付款即可',
                actions=[
                    PostbackAction(
                        label='~~~~~~~~~~~~~~~~~~~',
                        display_text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                   MessageAction(
                        label='門市地址',
                        text='高鐵門市地址'
                    ),
                    URIAction(
                        label='訂購表單',
                        uri='https://bit.ly/2Lhgrnx'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://scontent.ftpe8-2.fna.fbcdn.net/v/t1.0-9/79327003_3020675734617588_111192146333138944_n.jpg?_nc_cat=103&_nc_ohc=TtWIs9eKc-sAQmpge1FFJnBDoRemxWS3a0-LVR6sHLhT35_mS8IKxTsXg&_nc_ht=scontent.ftpe8-2.fna&oh=27b81efab9bcbdf4f8d92525515d998b&oe=5EB39E9E',
                title='美村本店(自取)',
                text='請填寫表單，完成後來電確認，取貨時付款即可',
                actions=[
                    PostbackAction(
                        label='~~~~~~~~~~~~~~~~~~~',
                        display_text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageAction(
                        label='門市地址',
                        text='美村本店地址'
                    ),
                    URIAction(
                        label='訂購表單',
                        uri='https://bit.ly/2sAgS4I'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://scontent.ftpe8-2.fna.fbcdn.net/v/t1.0-9/78918939_3020675737950921_6237532466555387904_n.jpg?_nc_cat=103&_nc_ohc=uxxSk9XOLYUAQmc7lzkDRhNhk_h3LuzTRyKHIboEsX2zHsU8rSeqA6H0g&_nc_ht=scontent.ftpe8-2.fna&oh=015d9b93ba1d4b91c68abba29933dca0&oe=5E7DC110',
                title='宅配預訂',
                text='全台冷凍宅配，請先填寫完訂單並來電確認交貨日期後再行匯款',
                actions=[
                    PostbackAction(
                        label='~~~~~~~~~~~~~~~~~~~',
                        display_text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageAction(
                        label='~~~~~~~~~~~~~~~~~~~',
                        text='message text1'
                    ),
                    URIAction(
                        label='訂購表單',
                        uri='https://bit.ly/2sAgS4I'
                    )
                ]
            )
        ]
        )
        )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
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
                        action=MessageAction(label='運費計算方式?', text="運費計算方式?")
                    ),
                    SeparatorComponent(),
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
                        action=MessageAction(label='期待新的產品推出', text="期待新的產品推出")
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
                        action=MessageAction(label='可以告訴我完整的訂購流程嗎?', text="可以告訴我完整的訂購流程嗎?")
                    )
                ]
            ) 
        )
        message = FlexSendMessage(alt_text="hello", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
        return

    if "高鐵門市地址" in msg:
        re = "台中高鐵站內摩斯漢堡對面"
    elif "美村本店地址" in msg:
        re = "台中市西區美村路一段596巷14號"
    

    

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=re))


if __name__ == "__main__":
    app.run()
