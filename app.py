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
                        label='postback1',
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
                        label='---------------------------',
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
                        label='postback1',
                        display_text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageAction(
                        label='message1',
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

    if "高鐵門市地址" in msg:
        re = "台中高鐵站內摩斯漢堡對面"
    elif "美村本店地址" in msg:
        re = "台中市西區美村路一段596巷14號"
    

    

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=re))


if __name__ == "__main__":
    app.run()
