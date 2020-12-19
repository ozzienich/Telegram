from telegram import Update, ParseMode 
from telegram.ext import Updater, CommandHandler, CallbackContext,  MessageHandler, Filters
import re
import os
import cm_client
from cm_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
cm_client.configuration.username = 'admin'
cm_client.configuration.password = 'admin'

api_host_drc = 'http://10.xx.xx.xx'
api_host_dc = 'http://10.xx.xx.xx'
port = '7180'
api_version = 'v33'
api_url_dc = api_host_dc + ':' + port + '/api/' + api_version
api_url_drc = api_host_drc + ':' + port + '/api/' + api_version
mo=''

#/CM_DC_CLUSTER
def cm_dc_cluster_command(update: Update, context: CallbackContext) -> None:
    chat_ids = update.message.chat_id
    api_client = cm_client.ApiClient(api_url_dc)
    cluster_api_instance = cm_client.ClustersResourceApi(api_client)
    api_response = cluster_api_instance.read_clusters(cluster_type='base',view='full')
    for cluster in api_response.items:
        mo = ('Site: <b>DC</b>:\n')
        mo = mo + ('Name: <b>'+ cluster.name+'</b>\n')
        mo = mo + ('Version: '+ cluster.full_version+ '\n')
        mo = mo + ('Status: '+ cluster.entity_status + '\n')
        mo = mo + ('Maintenance: '+ str(cluster.maintenance_mode) + '\n')
        mo = mo + ('URL: '+ cluster.cluster_url+ '\n')
        context.bot.send_message(chat_id=chat_ids,parse_mode=ParseMode.HTML,text=(mo))

#/CM_DRC_CLUSTER
def cm_drc_cluster_command(update: Update, context: CallbackContext) -> None:
    chat_ids = update.message.chat_id
    api_client = cm_client.ApiClient(api_url_drc)
    cluster_api_instance = cm_client.ClustersResourceApi(api_client)
    api_response = cluster_api_instance.read_clusters(view='full')
    for cluster in api_response.items:
        mo = ('Site: <b>DRC</b>:\n')
        mo = mo + ('Name: <b>'+ cluster.name+'</b>\n')
        mo = mo + ('Version: '+ cluster.full_version+ '\n')
        mo = mo + ('Status: '+ cluster.entity_status+ '\n')
        mo = mo + ('Maintenance: '+ str(cluster.maintenance_mode) + '\n')
        mo = mo + ('URL: '+ cluster.cluster_url+ '\n')
        context.bot.send_message(chat_id=chat_ids,parse_mode=ParseMode.HTML,text=(mo))

#/CM_clusterX1_HOST
def cm_clusterX1_host_command(update: Update, context: CallbackContext) -> None:
    chat_ids = update.message.chat_id
    api_client = cm_client.ApiClient(api_url_dc)
    api_instance = cm_client.ClustersResourceApi(api_client)
    api_response = api_instance.list_hosts('clusterX1')
    mo = ('Cluster: <b>clusterX1</b>:\n')
    for cluster in api_response.items:
        mo = mo + ('Host: '+ cluster.hostname+'\n')
        
    context.bot.send_message(chat_id=chat_ids,parse_mode=ParseMode.HTML,text=(mo))
        
#/CM_kafkaXX1_HOST
def cm_kafkaXX1_host_command(update: Update, context: CallbackContext) -> None:
    chat_ids = update.message.chat_id
    api_client = cm_client.ApiClient(api_url_dc)
    api_instance = cm_client.ClustersResourceApi(api_client)
    api_response = api_instance.list_hosts('kafkaXX1')
    print(api_response)
    mo = ('Cluster: <b>kafkaXX1</b>:\n')
    for cluster in api_response.items:
        mo = mo + ('Host: '+ cluster.hostname+'\n')
        
    context.bot.send_message(chat_id=chat_ids,parse_mode=ParseMode.HTML,text=(mo))
    
#/CM_clusterZ1_HOST
def cm_clusterZ1_host_command(update: Update, context: CallbackContext) -> None:
    chat_ids = update.message.chat_id
    api_client = cm_client.ApiClient(api_url_drc)
    api_instance = cm_client.ClustersResourceApi(api_client)
    api_response = api_instance.list_hosts('clusterZ1')
    print(api_response)
    mo = ('Cluster: <b>clusterZ1</b>:\n')
    for cluster in api_response.items:
        mo = mo + ('Host: '+ cluster.hostname+'\n')
        
    context.bot.send_message(chat_id=chat_ids,parse_mode=ParseMode.HTML,text=(mo))
        
#/CM_kafkaXX1drc_HOST
def cm_kafkaXX1drc_host_command(update: Update, context: CallbackContext) -> None:
    chat_ids = update.message.chat_id
    api_client = cm_client.ApiClient(api_url_drc)
    api_instance = cm_client.ClustersResourceApi(api_client)
    api_response = api_instance.list_hosts('kafkaXX1drc')
    print(api_response)
    mo = ('Cluster: <b>kafkaXX1drc</b>:\n')
    for cluster in api_response.items:
        mo = mo + ('Host: '+ cluster.hostname+'\n')
        
    context.bot.send_message(chat_id=chat_ids,parse_mode=ParseMode.HTML,text=(mo))
    

    
#/CM_clusterX1_services
def cm_clusterX1_services_command(update: Update, context: CallbackContext) -> None:
    chat_ids = update.message.chat_id
    api_client = cm_client.ApiClient(api_url_dc)
    api_instance = cm_client.ServicesResourceApi(api_client)
    api_response = api_instance.read_services('clusterX1')
    mo = ('Cluster: <b>clusterX1</b>:\n')
    for cluster in api_response.items:
        if (cluster.health_summary == 'GOOD'):
            mo = (mo + '\U00002705')
            
        mo = mo + ('[<b>' +cluster.display_name+'</b>] => '+ cluster.health_summary +'=> '+cluster.service_state + '\n')
        
    context.bot.send_message(chat_id=chat_ids,parse_mode=ParseMode.HTML,text=(mo))

#/CM_kafkaXX1_services
def cm_kafkaXX1_services_command(update: Update, context: CallbackContext) -> None:
    chat_ids = update.message.chat_id
    api_client = cm_client.ApiClient(api_url_dc)
    api_instance = cm_client.ServicesResourceApi(api_client)
    api_response = api_instance.read_services('kafkaXX1')
    mo = ('Cluster: <b>kafkaXX1</b>:\n')
    for cluster in api_response.items:
        if (cluster.health_summary == 'GOOD'):
            mo = (mo + '\U00002705')
            
        mo = mo + ('[<b>' +cluster.display_name+'</b>] => '+ cluster.health_summary +'=> '+cluster.service_state + '\n')
        
    context.bot.send_message(chat_id=chat_ids,parse_mode=ParseMode.HTML,text=(mo))

    
#/CM_clusterZ1_services
def cm_clusterZ1_services_command(update: Update, context: CallbackContext) -> None:
    chat_ids = update.message.chat_id
    api_client = cm_client.ApiClient(api_url_drc)
    api_instance = cm_client.ServicesResourceApi(api_client)
    api_response = api_instance.read_services('clusterZ1')
    mo = ('Cluster: <b>clusterZ1</b>:\n')
    for cluster in api_response.items:
        if (cluster.health_summary == 'GOOD'):
            mo = (mo + '\U00002705')
            
        mo = mo + ('[<b>' +cluster.display_name+'</b>] => '+ cluster.health_summary +'=> '+cluster.service_state + '\n')
        
    context.bot.send_message(chat_id=chat_ids,parse_mode=ParseMode.HTML,text=(mo))

#/CM_kafkaXX1drc_services
def cm_kafkaXX1drc_services_command(update: Update, context: CallbackContext) -> None:
    chat_ids = update.message.chat_id
    api_client = cm_client.ApiClient(api_url_drc)
    api_instance = cm_client.ServicesResourceApi(api_client)
    api_response = api_instance.read_services('kafkaXX1drc')
#    print(api_response)
    mo = ('Cluster: <b>kafkaXX1drc</b>:\n')
    for cluster in api_response.items:
        if (cluster.health_summary == 'GOOD'):
            mo = (mo + '\U00002705')
            
        mo = mo + ('[<b>' +cluster.display_name+'</b>] => '+ cluster.health_summary +'=> '+cluster.service_state + '\n')
        
    context.bot.send_message(chat_id=chat_ids,parse_mode=ParseMode.HTML,text=(mo))
        
    
def start (update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Cloudera bot started!')
    
def unknown(update, context):
    context.bot.send_message(chat_id=chat_ids,parse_mode=ParseMode.HTML,text='sorry. unknown command \U0001F61C')   


REQUEST_KWARGS={ 'proxy_url': 'http://xx.xx.xx.xx:8080/',}

updater = Updater("TOKEENN", use_context=True, request_kwargs=REQUEST_KWARGS)

unknown_handler = MessageHandler(Filters.command, unknown)

updater.dispatcher.add_handler(CommandHandler('cm',start))
updater.dispatcher.add_handler(CommandHandler('cm_dc_cluster',cm_dc_cluster_command))
updater.dispatcher.add_handler(CommandHandler('cm_drc_cluster',cm_drc_cluster_command))
updater.dispatcher.add_handler(CommandHandler('cm_clusterX1_host',cm_clusterX1_host_command))
updater.dispatcher.add_handler(CommandHandler('cm_kafkaXX1_host',cm_kafkaXX1_host_command))
updater.dispatcher.add_handler(CommandHandler('cm_clusterZ1_host',cm_clusterZ1_host_command))
updater.dispatcher.add_handler(CommandHandler('cm_kafkaXX1drc_host',cm_kafkaXX1drc_host_command))
updater.dispatcher.add_handler(CommandHandler('cm_clusterX1_services',cm_clusterX1_services_command))
updater.dispatcher.add_handler(CommandHandler('cm_kafkaXX1_services',cm_kafkaXX1_services_command))
updater.dispatcher.add_handler(CommandHandler('cm_clusterZ1_services',cm_clusterZ1_services_command))
updater.dispatcher.add_handler(CommandHandler('cm_kafkaXX1drc_services',cm_kafkaXX1drc_services_command))



updater.dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()

