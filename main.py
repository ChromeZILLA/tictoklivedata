from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, GiftEvent
import winsound

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@thealiceirving")


# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)


# Notice no decorator?
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")


@client.on("gift")
async def on_gift(event: GiftEvent):
    # If it's type 1 and the streak is over
    if event.gift.gift_type == 1:
        if event.gift.repeat_end == 1:
            print(
                f"{event.user.uniqueId} sent {event.gift.repeat_count}x \"{event.gift.extended_gift.name} \"{event.gift.giftId}")


    # It's not type 1, which means it can't have a streak & is automatically over
    elif event.gift.gift_type != 1:
        print(f"{event.user.uniqueId} sent \"{event.gift.extended_gift.name}\"")


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
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        print('5826 playing sound using  playsound')


@client.on("gift")
async def on_gift(event: GiftEvent):
    if event.gift.giftId == 5826:
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        print('5826 playing sound using  playsound')


# Define handling an event via "callback"
client.add_listener("comment", on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()