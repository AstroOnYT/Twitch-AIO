import os
import sys
import time
import socket
import random
import clipboard
import threading
from requests_futures.sessions import FuturesSession

session = FuturesSession()
tokens = []

if sys.platform == "linux":
    clear = lambda: os.system("clear")
else:
    clear = lambda: os.system("cls & mode 80,24 & title [TwitchAIO] By Dropout")

config = {
    "Purple": "\x1b[38;5;99m",
    "White": "\x1b[0m"
}

banner = f"""
                           \x1b[38;2;142;66;254m╔\x1b[38;2;145;65;251m╦\x1b[38;2;148;64;248m╗\x1b[38;2;151;63;245m╦\x1b[38;2;154;62;242m \x1b[38;2;157;61;239m╦\x1b[38;2;160;60;236m╦\x1b[38;2;163;59;233m╔\x1b[38;2;166;58;230m╦\x1b[38;2;169;57;227m╗\x1b[38;2;172;56;224m╔\x1b[38;2;175;55;221m═\x1b[38;2;178;54;218m╗\x1b[38;2;181;53;215m╦\x1b[38;2;184;52;212m \x1b[38;2;187;51;209m╦\x1b[38;2;190;50;206m \x1b[38;2;193;49;203m \x1b[38;2;196;48;200m╔\x1b[38;2;199;47;197m═\x1b[38;2;202;46;194m╗\x1b[38;2;205;45;191m╦\x1b[38;2;208;44;188m╔\x1b[38;2;211;43;185m═\x1b[38;2;214;42;182m╗\x1b[38;2;217;41;179m
                           \x1b[38;2;142;66;254m \x1b[38;2;145;65;251m║\x1b[38;2;148;64;248m \x1b[38;2;151;63;245m║\x1b[38;2;154;62;242m║\x1b[38;2;157;61;239m║\x1b[38;2;160;60;236m║\x1b[38;2;163;59;233m \x1b[38;2;166;58;230m║\x1b[38;2;169;57;227m \x1b[38;2;172;56;224m║\x1b[38;2;175;55;221m \x1b[38;2;178;54;218m \x1b[38;2;181;53;215m╠\x1b[38;2;184;52;212m═\x1b[38;2;187;51;209m╣\x1b[38;2;190;50;206m \x1b[38;2;193;49;203m \x1b[38;2;196;48;200m╠\x1b[38;2;199;47;197m═\x1b[38;2;202;46;194m╣\x1b[38;2;205;45;191m║\x1b[38;2;208;44;188m║\x1b[38;2;211;43;185m \x1b[38;2;214;42;182m║\x1b[38;2;217;41;179m
                           \x1b[38;2;142;66;254m \x1b[38;2;145;65;251m╩\x1b[38;2;148;64;248m \x1b[38;2;151;63;245m╚\x1b[38;2;154;62;242m╩\x1b[38;2;157;61;239m╝\x1b[38;2;160;60;236m╩\x1b[38;2;163;59;233m \x1b[38;2;166;58;230m╩\x1b[38;2;169;57;227m \x1b[38;2;172;56;224m╚\x1b[38;2;175;55;221m═\x1b[38;2;178;54;218m╝\x1b[38;2;181;53;215m╩\x1b[38;2;184;52;212m \x1b[38;2;187;51;209m╩\x1b[38;2;190;50;206m \x1b[38;2;193;49;203m \x1b[38;2;196;48;200m╩\x1b[38;2;199;47;197m \x1b[38;2;202;46;194m╩\x1b[38;2;205;45;191m╩\x1b[38;2;208;44;188m╚\x1b[38;2;211;43;185m═\x1b[38;2;214;42;182m╝
\033[4m\x1b[38;2;142;66;254m \x1b[38;2;143;66;253m \x1b[38;2;144;66;252m \x1b[38;2;145;66;251m \x1b[38;2;146;66;250m \x1b[38;2;147;66;249m \x1b[38;2;148;66;248m \x1b[38;2;149;66;247m \x1b[38;2;150;66;246m \x1b[38;2;151;66;245m \x1b[38;2;152;66;244m \x1b[38;2;153;66;243m \x1b[38;2;154;66;242m \x1b[38;2;155;66;241m \x1b[38;2;156;66;240m \x1b[38;2;157;66;239m \x1b[38;2;158;66;238m \x1b[38;2;159;66;237m \x1b[38;2;160;66;236m \x1b[38;2;161;66;235m \x1b[38;2;162;66;234m \x1b[38;2;163;66;233m \x1b[38;2;164;66;232m \x1b[38;2;165;66;231m \x1b[38;2;166;66;230m \x1b[38;2;167;66;229m \x1b[38;2;168;66;228m \x1b[38;2;169;66;227m \x1b[38;2;170;66;226m \x1b[38;2;171;66;225m \x1b[38;2;172;66;224m \x1b[38;2;173;66;223m \x1b[38;2;174;66;222m \x1b[38;2;175;66;221m \x1b[38;2;176;66;220m \x1b[38;2;177;66;219m \x1b[38;2;178;66;218m \x1b[38;2;179;66;217m \x1b[38;2;180;66;216m \x1b[38;2;181;66;215m \x1b[38;2;182;66;214m \x1b[38;2;183;66;213m \x1b[38;2;184;66;212m \x1b[38;2;185;66;211m \x1b[38;2;186;66;210m \x1b[38;2;187;66;209m \x1b[38;2;188;66;208m \x1b[38;2;189;66;207m \x1b[38;2;190;66;206m \x1b[38;2;191;66;205m \x1b[38;2;192;66;204m \x1b[38;2;193;66;203m \x1b[38;2;194;66;202m \x1b[38;2;195;66;201m \x1b[38;2;196;66;200m \x1b[38;2;197;66;199m \x1b[38;2;198;66;198m \x1b[38;2;199;66;197m \x1b[38;2;200;66;196m \x1b[38;2;201;66;195m \x1b[38;2;202;66;194m \x1b[38;2;203;66;193m \x1b[38;2;204;66;192m \x1b[38;2;205;66;191m \x1b[38;2;206;66;190m \x1b[38;2;207;66;189m \x1b[38;2;208;66;188m \x1b[38;2;209;66;187m \x1b[38;2;210;66;186m \x1b[38;2;211;66;185m \x1b[38;2;212;66;184m \x1b[38;2;213;66;183m \x1b[38;2;214;66;182m \x1b[38;2;215;66;181m \x1b[38;2;216;66;180m \x1b[38;2;217;66;179m \x1b[38;2;218;66;178m \x1b[38;2;219;66;177m \x1b[38;2;220;66;176m \x1b[38;2;221;66;175m \033[0m
"""
options = f"""
                           {config["Purple"]}[{config["White"]}1{config["Purple"]}]{config["White"]} Get Channel ID
                           {config["Purple"]}[{config["White"]}2{config["Purple"]}]{config["White"]} Follow Channel
                           {config["Purple"]}[{config["White"]}3{config["Purple"]}]{config["White"]} Unfollow Channel
"""

class Twitch:

    def Check(token):
        headers = {'Client-Id': "kimne78kx3ncx6brgo4mv6wki5h1ko", "Authorization": f"OAuth {token}"}
        json = [{"operationName":"Chat_ShareBitsBadgeTier_ChannelData","variables":{"channelLogin":"Dropout1337"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"95383deae2b82f718b9d713ca433807ff60dffa8c834e2ae92abdfeb55586fc4"}}},{"operationName":"Chat_ShareResub_ChannelData","variables":{"channelLogin":"Dropout1337"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"1cef2e84b602f767839e5ffd489e81536e9d11e0be250bb85a17974cedad8f54"}}}]
        r = session.post(f"https://gql.twitch.tv/gql", headers=headers, json=json).result()
        if "id" in r.text:
            return True
        else:
            return False

    def Channel_ID(token, target):
        headers = {'Client-Id': "kimne78kx3ncx6brgo4mv6wki5h1ko", "Authorization": f"OAuth {token}"}
        json = [{"operationName":"Chat_ShareBitsBadgeTier_ChannelData","variables":{"channelLogin":target},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"95383deae2b82f718b9d713ca433807ff60dffa8c834e2ae92abdfeb55586fc4"}}},{"operationName":"Chat_ShareResub_ChannelData","variables":{"channelLogin":target},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"1cef2e84b602f767839e5ffd489e81536e9d11e0be250bb85a17974cedad8f54"}}}]
        r = session.post(f"https://gql.twitch.tv/gql", headers=headers, json=json).result()
        if 'user' in r.text:
            if r.json()[0]["data"]["user"] == None:
                return False
            else:
                return r.json()[0]["data"]["user"]["id"]
        else:
            return False

    def Follow(channel_id, token):
        if len(token) == 30:
            hide_part = token[20:]
            hidden_token = token.replace(hide_part, "**********")
            headers = {'Client-Id': "kimne78kx3ncx6brgo4mv6wki5h1ko", 'Authorization': f"OAuth {token}"}
            json = [{"operationName":"FollowButton_FollowUser","variables":{"input":{"disableNotifications":False,"targetID":channel_id}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"3efee1acda90efdff9fef6e6b4a29213be3ee490781c5b54469717b6131ffdfe"}}}]
            r = session.post('https://gql.twitch.tv/gql', json=json, headers=headers).result()
            if "followUser" in r.text:
                print(f'                           {config["Purple"]}[{config["White"]}Success{config["Purple"]}]{config["White"]} {hidden_token}')
            else:
                print(f'                           {config["Purple"]}[{config["White"]}Failed{config["Purple"]}]{config["White"]} {hidden_token}')
        else:
            print(f'                           {config["Purple"]}[{config["White"]}Fake{config["Purple"]}]{config["White"]} {hidden_token}')

    def Unfollow(channel_id, token):
        headers = {'Client-Id': "kimne78kx3ncx6brgo4mv6wki5h1ko", 'Authorization': f"OAuth {token}"}
        json = {"operationName":"FollowButton_UnfollowUser","variables":{"input":{"targetID":channel_id}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"d7fbdb4e9780dcdc0cc1618ec783309471cd05a59584fc3c56ea1c52bb632d41"}}}
        r = session.post('https://gql.twitch.tv/gql', json=json, headers=headers).result()
        if "unfollowUser" in r.text:
            return True
        else:
            return False

class TwitchAIO:

    def Load_Tokens():
        for line in open('Tokens.txt'):
            tokens.append(line.replace('\n', ''))
        return len(tokens)

    def Menu():
        clear()
        print(banner+options)
        choice = input(f'                           {config["Purple"]}[{config["White"]}Option{config["Purple"]}]{config["White"]} ')
        if choice == "1":
            clear()
            print(banner)
            channel_name = input(f'                           {config["Purple"]}[{config["White"]}Channel Name{config["Purple"]}]{config["White"]} ')
            channel_id = Twitch.Channel_ID(random.choice(tokens), channel_name)
            if channel_id == False:
                print(f'                           {config["Purple"]}[{config["White"]}Error{config["Purple"]}]{config["White"]} Unable to fetch channel id, please try again.')
            else:
                clipboard.copy(channel_id)
                print(f'                           {config["Purple"]}[{config["White"]}Success{config["Purple"]}]{config["White"]} Copied to clipboard.')
            time.sleep(1)
            TwitchAIO.Menu()
        elif choice == "2":
            clear()
            print(banner)
            channel_id = input(f'                           {config["Purple"]}[{config["White"]}Channel ID{config["Purple"]}]{config["White"]} ')
            running = []
            print()
            for x in range(len(tokens)):
                t = threading.Thread(target=Twitch.Follow, args=(channel_id, tokens[x]))
                t.start()
                running.append(t)

            for x in running:
                x.join()

            TwitchAIO.Menu()

        elif choice == "3":
            clear()
            print(banner)
            channel_id = input(f'                           {config["Purple"]}[{config["White"]}Channel ID{config["Purple"]}]{config["White"]} ')
            running = []
            print()
            for x in range(len(tokens)):
                t = threading.Thread(target=Twitch.Unfollow, args=(channel_id, tokens[x]))
                t.start()
                running.append(t)

            for x in running:
                x.join()

            TwitchAIO.Menu()

        else:
            TwitchAIO.Menu()

if __name__ == "__main__":
    TwitchAIO.Load_Tokens()
    TwitchAIO.Menu()