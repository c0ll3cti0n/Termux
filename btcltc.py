U
    �^�  �                   @   s�   d dl Z d dlZd dlZd dlZd dlZd dlZd dlZejejd� d dl	m
Z
mZ d dlmZ d dlmZ d dlmZ d dlmZmZ edd	� e�ejd
kr�dnd� dZdZdZdZdZdZdZdd� Zdd� Ze � � �!e� � dS )�    N)�level)�TelegramClient�events)�JoinChannelRequest)�GetBotCallbackAnswerRequest)�datetime)�Fore�initT)Z	autoreset�nt�cls�cleari,8 Z db55ad67a98df35667ca788b97f771f5ZFree_Bitcoin_Claim_Botz@Free_Bitcoin_Claim_BotZFree_Litecoin_Claim_Botz@Free_Litecoin_Claim_Botzfree btc and ltc claim botc                 C   s2   t dtj t�� �d��  tj d| � � � d S )N�[z%H:%M:%Sz] )�printr   �MAGENTAr   Znow�strftime�RESET)�message� r   �	btcltc.py�print_msg_time   s    r   c                  �   sl  t tjd tj � t tjd tj � t tjd tj � ttj�dk rjt d� t d� td�} t	d� tjd }d	}d
}t
j�d�s�t
�d� td| tt�}|�|�I d H  |�� I d H }ttjd|j� d� t tj � d}|dk�rZ|�t|�I d H  ttjd tj � t�d� |�t|�I d H  ttjd tj � t�d� |d7 }q�|�� I d H  d S )Nz ________________ u<   --------------Recoded during morning walk----🚶 🚶 🚶 z ________________
�   z#Usage: python start.py phone_numberz)-> Input number in international format 
zPress any key to exit...�   u
   🎰 Bonusu   🎰 Claim LTCZsessionzsession/zWelcome : (z) to i'  zClaimed Free BTC �   zClaimed Free LTCi�  )r   r   ZBLUEr   r   �len�sys�argv�input�exit�os�path�exists�mkdirr   �api_id�api_hash�startZget_mer   Z
first_name�lolZsend_message�forecast_group�time�sleep�forecast_group1Zrun_until_disconnected)�eZphone_numberZchoice1Zchoice2Zclient�me�ir   r   r   �main!   s6    

"



r-   )"ZasyncioZlogging�rer'   r   r   ZrandomZbasicConfigZERRORZtelethonr   r   Ztelethon.tl.functions.channelsr   Ztelethon.tl.functions.messagesr   r   Zcoloramar   r	   Z	color_ama�system�namer"   r#   Zforecast_channelr&   Zforecast_channel1r)   r%   r   r-   Zget_event_loopZrun_until_completer   r   r   r   �<module>   s0   
*