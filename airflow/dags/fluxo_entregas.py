import os
import sys
import time

from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

from airflow_utils import set_dag_id


with DAG(dag_id=set_dag_id(__file__),
         schedule_interval="@daily",
         start_date=days_ago(1),
         max_active_tasks=1) as dag:

    start = DummyOperator(task_id='start')

    limpar_e_tratar = PythonOperator(task_id='limpar_e_tratar_zona_curated', python_callable=lambda: time.sleep(5))

    relatorio_1 = PythonOperator(task_id='relatorio_1_zona_analytics', python_callable=lambda: time.sleep(5))
    catalogar_relatorio_1 = PythonOperator(task_id='catalogar_relatorio_1', python_callable=lambda: time.sleep(5))
    exportar_relatorio_1_para_dw = PythonOperator(task_id='exportar_relatorio_1_para_dw', python_callable=lambda: time.sleep(5))

    relatorio_2 = PythonOperator(task_id='relatorio_2_zona_analytics', python_callable=lambda: time.sleep(5))
    catalogar_relatorio_2 = PythonOperator(task_id='catalogar_relatorio_2', python_callable=lambda: time.sleep(5))
    exportar_relatorio_2_para_dw = PythonOperator(task_id='exportar_relatorio_2_para_dw', python_callable=lambda: time.sleep(5))

    end = DummyOperator(task_id='end')

    start >> limpar_e_tratar

    limpar_e_tratar >> relatorio_1 >> catalogar_relatorio_1 >> exportar_relatorio_1_para_dw >> end
    limpar_e_tratar >> relatorio_2 >> catalogar_relatorio_2 >> exportar_relatorio_2_para_dw >> end
