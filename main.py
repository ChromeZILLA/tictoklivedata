from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, GiftEvent
import winsound
import mysql.connector
import sqlite3 as sql

# Creating connection object
mydb = mysql.connector.connect(
    host="192.168.2.100",
    user="jbrooks",
    password="Chrome",
    database = "geeksforgeeks"
)

cursor = mydb.cursor()

# Creating a table called 'gfg' in the
# 'geeksforgeeks' database
# cursor.execute("CREATE TABLE username (name VARCHAR(255), user_name VARCHAR(255))")
# cursor.execute("CREATE TABLE nikki (name VARCHAR(255), user_name VARCHAR(255))")



# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@katrinavianna2")


# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)


# Notice no decorator?
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")

@client.on("comment")
async def on_connect(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")
    add_username = ("INSERT INTO username" "(user_name) "
                          "VALUES (%(emp_no)s)")
    data_username = {
        'emp_no': event.user.nickname,
    }
    cursor.execute(add_username, data_username)
    mydb.commit()

@client.on("gift")
async def on_gift(event: GiftEvent):
    # If it's type 1 and the streak is over
    if event.gift.gift_type == 1:
        if event.gift.repeat_end == 1:
            print(
                f"{event.user.uniqueId} sent {event.gift.repeat_count}x \"{event.gift.extended_gift.name} \"{event.gift.giftId}")
            add_username = ("INSERT INTO gift" "(name, user_name) "
                            "VALUES (%(giftName)s, %(userName)s)")
            data_username = {
                'giftName': event.gift.extended_gift.name,
                'userName': event.user.nickname,
            }
            cursor.execute(add_username, data_username)
            mydb.commit()

    # It's not type 1, which means it can't have a streak & is automatically over
    elif event.gift.gift_type != 1:
        print(f"{event.user.uniqueId} sent \"{event.gift.extended_gift.name}\"")
        add_username = ("INSERT INTO gift" "(name, user_name) "
                        "VALUES (%(giftName)s, %(userName)s)")
        data_username = {
            'giftName': event.gift.extended_gift.name,
            'userName': event.user.nickname,
        }
        cursor.execute(add_username, data_username)
        mydb.commit()


@client.on("gift")
async def on_gift(event: GiftEvent):
    if event.gift.gift_type != 1:
        print(f"{event.gift.giftId}")


@client.on("gift")
async def on_gift(event: GiftEvent):
    if event.gift.giftId == 6200:
        print('6200 playing sound using  playsound')


@client.on("gift")
async def on_gift(event: GiftEvent):
    if event.gift.giftId == 5655:
        print('5655 playing sound using  playsound')
        add_username = ("INSERT INTO gift" "(name, user_name) "
                        "VALUES (%(giftName)s, %(userName)s)")
        data_username = {
            'giftName': event.gift.extended_gift.name,
            'userName': event.user.nickname,
        }
        cursor.execute(add_username, data_username)
        mydb.commit()

@client.on("gift")
async def on_gift(event: GiftEvent):
    if event.gift.giftId == 5826:
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        print('5826 playing sound using  playsound')



if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()