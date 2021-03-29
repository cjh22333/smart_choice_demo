1. Introduction
	This demo is an assignment to demonstrate a bit my understanding, creativity and technical ability in django development. The stock data is from Juquant SDK.

2. Prerequisite
	1. Django > 3.1.6
	2. Pyside2 >=5.15.2
    3. PyQt5    >=5.15.4
    4. jqdatasdk >1.8.4

3. Project structure
	1. Frontend:
			©¦  frame.py
©¦  main.py
©¦  tree.txt
©¦  
©À©¤.idea
©¦  ©¦  .gitignore
©¦  ©¦  misc.xml
©¦  ©¦  modules.xml
©¦  ©¦  Stock_qt.iml
©¦  ©¦  workspace.xml
©¦  ©¦  
©¦  ©¸©¤inspectionProfiles
©¦          profiles_settings.xml
©¦          
©À©¤img
©¦      tubiao.jpg
©¦      
©À©¤lib
©¦  ©¦  share_info.py
©¦  ©¦  __init__.py
©¦  ©¦  
©¦  ©¸©¤__pycache__
©¦          share_info.cpython-37.pyc
©¦          __init__.cpython-37.pyc
©¦          
©¸©¤UI
        login.ui
        main.ui
        portfolio.ui
        trade.ui
		
	
 2. Backend
		©¦  db.sqlite3
©¦  manage.py
©¦  tree.txt
©¦  
©À©¤.idea
©¦  ©¦  .gitignore
©¦  ©¦  dataSources.local.xml
©¦  ©¦  dataSources.xml
©¦  ©¦  misc.xml
©¦  ©¦  modules.xml
©¦  ©¦  stock_django.iml
©¦  ©¦  workspace.xml
©¦  ©¦  
©¦  ©À©¤dataSources
©¦  ©¦      4abd18d5-c7dc-4f8d-93ac-4d03a15aa65b.xml
©¦  ©¦      
©¦  ©¸©¤inspectionProfiles
©¦          profiles_settings.xml
©¦          
©À©¤lib
©¦  ©¦  serializer.py
©¦  ©¦  __init__.py
©¦  ©¦  
©¦  ©¸©¤__pycache__
©¦          serializer.cpython-37.pyc
©¦          __init__.cpython-37.pyc
©¦          
©À©¤stock_be
©¦  ©¦  admin.py
©¦  ©¦  apps.py
©¦  ©¦  models.py
©¦  ©¦  tests.py
©¦  ©¦  views.py
©¦  ©¦  __init__.py
©¦  ©¦  
©¦  ©À©¤migrations
©¦  ©¦  ©¦  0001_initial.py
©¦  ©¦  ©¦  0002_auto_20210323_0003.py
©¦  ©¦  ©¦  0003_watch_list.py
©¦  ©¦  ©¦  0004_auto_20210324_1129.py
©¦  ©¦  ©¦  0005_user_stock_pofolio.py
©¦  ©¦  ©¦  0006_auto_20210328_2015.py
©¦  ©¦  ©¦  0007_user_stock_pofolio_settle.py
©¦  ©¦  ©¦  0008_transaction_action.py
©¦  ©¦  ©¦  0009_auto_20210328_2254.py
©¦  ©¦  ©¦  0010_cash_account.py
©¦  ©¦  ©¦  0011_transaction_action_date.py
©¦  ©¦  ©¦  0012_auto_20210329_1624.py
©¦  ©¦  ©¦  __init__.py
©¦  ©¦  ©¦  
©¦  ©¦  ©¸©¤__pycache__
©¦  ©¦          0001_initial.cpython-37.pyc
©¦  ©¦          0002_auto_20210323_0003.cpython-37.pyc
©¦  ©¦          0003_watch_list.cpython-37.pyc
©¦  ©¦          0004_auto_20210324_1129.cpython-37.pyc
©¦  ©¦          0005_user_stock_pofolio.cpython-37.pyc
©¦  ©¦          0006_auto_20210328_2015.cpython-37.pyc
©¦  ©¦          0007_user_stock_pofolio_settle.cpython-37.pyc
©¦  ©¦          0008_transaction_action.cpython-37.pyc
©¦  ©¦          0009_auto_20210328_2254.cpython-37.pyc
©¦  ©¦          0010_cash_account.cpython-37.pyc
©¦  ©¦          0011_transaction_action_date.cpython-37.pyc
©¦  ©¦          0012_auto_20210329_1624.cpython-37.pyc
©¦  ©¦          __init__.cpython-37.pyc
©¦  ©¦          
©¦  ©¸©¤__pycache__
©¦          admin.cpython-37.pyc
©¦          apps.cpython-37.pyc
©¦          models.cpython-37.pyc
©¦          views.cpython-37.pyc
©¦          __init__.cpython-37.pyc
©¦          
©À©¤stock_django
©¦  ©¦  asgi.py
©¦  ©¦  settings.py
©¦  ©¦  urls.py
©¦  ©¦  wsgi.py
©¦  ©¦  __init__.py
©¦  ©¦  
©¦  ©¸©¤__pycache__
©¦          settings.cpython-37.pyc
©¦          urls.cpython-37.pyc
©¦          wsgi.cpython-37.pyc
©¦          __init__.cpython-37.pyc
©¦          
©¸©¤templates


4. Frameworks 
	1. Django
     2. PyQT5

5. Author
	Rein Chen




		
	