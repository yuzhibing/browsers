

### python

pip install -r requirements.txt


### UI
    npm install yarn -g
    yarn install
    yarn run build
    webpack.dev.config.js //修改server ip
### 数据库脚本
    sql/ut.sql

### 第一次运行需要同步历史数据(多线程同步数据时间比较长)
    job/config.py //---数据库、守护进程配置文件
    nohup python -u thread_run.py >log_thread.txt 2>&1 &
    
### 同步完历史数据后，使用job_run.py同步数据（单机运行）
    nohup python -u job_run.py >log_job.txt 2>&1 &
    
### app service run
    config.py //---数据库配置文件
    nohup python -u app.py >log_app.txt 2>&1 &
    
    