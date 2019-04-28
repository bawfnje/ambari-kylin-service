from resource_management import *
from resource_management.libraries.script.script import Script
from resource_management.libraries.functions.default import default
import os

# server configurations
config = Script.get_config()
service_packagedir = os.path.realpath(__file__).split('/scripts')[0]
tmp_dir = Script.get_tmp_dir()

ambari_server_hostname = config['ambariLevelParams']['ambari_server_host']
kylin_download = os.path.join('http://', ambari_server_hostname, 'xdata-epel/centos7/7.3-000/kylin-2.6.0.tar.gz')

kylin_install_dir = config['configurations']['kylin']['kylin_install_dir']
kylin_log_dir = config['configurations']['kylin']['kylin_log_dir']
kylin_pid_dir = config['configurations']['kylin']['kylin_pid_dir']
kylin_pid_file = format("{kylin_pid_dir}/kylin.pid")

kylin_web_port = config['configurations']['kylin']['kylin_web_port']

kylin_properties = config['configurations']['kylin']['kylin_properties']

# kylin web timezone
kylin_web_timezone = config['configurations']['kylin']['kylin_web_timezone']
# kylin_web_cross_domain_enabled
kylin_web_cross_domain_enabled = config['configurations']['kylin']['kylin_web_cross_domain_enabled']
if (kylin_web_cross_domain_enabled):
    kylin_web_cross_domain_enabled = 'true'
else:
    kylin_web_cross_domain_enabled = 'false'

current_host_name = config['agentLevelParams']['hostname']
server_mode = "query"
server_masters = config['clusterHostInfo']['kylin_all_hosts'][0]
server_clusters_arr = config['clusterHostInfo']['kylin_all_hosts'] + (
    config['clusterHostInfo'].has_key('kylin_query_hosts') and config['clusterHostInfo']['kylin_query_hosts'] or [])

server_clusters = ','.join(i + ":" + kylin_web_port for i in server_clusters_arr)
kylin_servers = ';'.join("server " + i + ":" + kylin_web_port for i in server_clusters_arr) + ";"

# hive
hive_server_host = default("/clusterHostInfo/hive_server_hosts", ['localhost'])[0]
hive_server_port = default('/configurations/hive-site/hive.server2.thrift.port', "10000")
