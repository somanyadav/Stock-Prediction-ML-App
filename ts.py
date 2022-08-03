import streamlit as st
import pandas as pd
import sqlite3 as sq
import datetime
import yfinance as yf
from preprocess import preprocessing
import warnings
warnings.filterwarnings("ignore")

db = sq.connect('stocks.db')

# get country
query = "SELECT DISTINCT(Country) FROM tkrinfo;"
country = pd.read_sql_query(query, db)
choice_country = st.sidebar.selectbox("Pick country", country)

# get exchange
query = "SELECT DISTINCT(Exchange) FROM tkrinfo WHERE Country = '" + choice_country + "'"
exchange = pd.read_sql_query(query, db)
choice_exchange = st.sidebar.selectbox("Pick exchange", exchange, index = 1)

# get stock name
query = "SELECT DISTINCT(Name) FROM tkrinfo WHERE Exchange = '" + choice_exchange + "'"
name = pd.read_sql_query(query, db)
choice_name = st.sidebar.selectbox("Pick the Stock", name)

# get stock tickr
query = "SELECT DISTINCT(Ticker) FROM tkrinfo WHERE Exchange = '" + choice_exchange + "'" + "and Name = '" + choice_name + "'"
ticker_name = pd.read_sql_query(query, db)
ticker_name = ticker_name.loc[0][0]





interval = st.sidebar.selectbox("Interval", ['1d', '1wk', '1mo', '3mo'])

period = st.sidebar.selectbox("Period",['1mo','3mo','6mo','1y','2y','5y','10y','max'],index = 2)

stock = yf.Ticker(str(ticker_name))
data = stock.history(interval=interval, period=period)

if len(data)==0:
    st.write("Unable to retrieve data.This ticker may no longer be in use. Try some other stock")
else:

    
    data = preprocessing(data,interval)

    if period == '1mo' or period == '3mo':
        horizon = st.sidebar.slider("Forecast horizon",1,15,5)
    else:
        if interval == '1d' or interval == '1wk':
            horizon = st.sidebar.slider("Forecast horizon", 1, 30, 5)
        else:
            horizon = st.sidebar.slider("Forecast horizon", 1, 15, 5)

    model = st.selectbox('Model',['Simple Exponential Smoothing','Halt Model','Holt-Winter Model','Auto Regressive Model',
                                  'Moving Average Model','ARMA Model', 'ARIMA Model','AutoARIMA',
                                  'Linear Regression','Random Forest', 'Gradient Boosting','Support Vector Machines',
                                  ])

    if model=='Simple Exponential Smoothing':
        col1,col2 = st.columns(2)
        with col1:
            alpha_high = st.slider("Alpha_high",0.0,1.0,0.20)
        with col2:
            alpha_low = st.slider("Alpha_low",0.0,1.0,0.25)
        from SES import SES_model
        data_final, smap_low, smap_high, optim_alpha_high, optim_alpha_low = SES_model(data,horizon,alpha_high,alpha_low)

#data_final
        st.line_chart(data_final[['High','Forecast_High','Low','Forecast_Low']])
        col1,col2 = st.columns(2)
        with col1:
            st.write("SMAPE for High: {}".format(smap_high))
            st.write("Optimal Alpha for High : {} ".format(optim_alpha_high))
        with col2:
            st.write("SMAPE for Low: {}".format(smap_low))
            st.write("Optimal Alpha for Low: {} ".format(optim_alpha_low))

    elif model == 'Halt Model':
        col1, col2,col3,col4 = st.columns(4)
        with col1:
            level_high = st.slider("Level High", 0.0, 1.0, 0.20)
        with col2:
            trend_high = st.slider("Trend high", 0.0, 1.0, 0.20)
        with col3:
            level_low = st.slider("Level low", 0.0, 1.0, 0.20)
        with col4:
            trend_low = st.slider("Trend Low", 0.0, 1.0, 0.20)
        from SES import Holt_model
        data_final,smap_low,smap_high,optim_level_high,optim_level_low,optim_trend_high,optim_trend_low = Holt_model(data,horizon
                                                                        ,level_high,level_low,trend_high,trend_low)
        st.line_chart(data_final[['High', 'Forecast_High', 'Low', 'Forecast_Low']])
        col1, col2 = st.columns(2)
        with col1:
            st.write("SMAPE for High: {}".format(smap_high))
            st.write("Optimal Level for High : {} ".format(optim_level_high))
            st.write("Optimal Trend for High : {} ".format(optim_trend_high))
        with col2:
            st.write("SMAPE for Low: {}".format(smap_low))
            st.write("Optimal Level for Low: {} ".format(optim_level_low))
            st.write("Optimal Trend for Low: {} ".format(optim_trend_low))


    elif model == 'Holt-Winter Model':
        col1, col2 = st.columns(2)
        with col1:
            level_high = st.slider("Level High", 0.0, 1.0, 0.20)
            trend_high = st.slider("Trend high", 0.0, 1.0, 0.20)
            season_high = st.slider("Seasonal high", 0.0, 1.0, 0.20)
        with col2:
            level_low = st.slider("Level low", 0.0, 1.0, 0.20)
            trend_low = st.slider("Trend Low", 0.0, 1.0, 0.20)
            season_low = st.slider("Seasonal Low", 0.0, 1.0, 0.20)
        from SES import Holt_Winter_Model
        data_final, smap_low, smap_high, optim_level_high, optim_level_low, optim_trend_high, optim_trend_low, optim_season_high, optim_season_low = Holt_Winter_Model(data,horizon, level_high, level_low,trend_high,trend_low,season_high,season_low)

        st.line_chart(data_final[['High', 'Forecast_High', 'Low', 'Forecast_Low']])
        col1, col2 = st.columns(2)
        with col1:
            st.write("SMAPE for High: {}".format(smap_high))
            st.write("Optimal Level for High : {} ".format(optim_level_high))
            st.write("Optimal Trend for High : {} ".format(optim_trend_high))
            st.write("Optimal Seasonal smoothing for high: {}".format(optim_season_high))
        with col2:
            st.write("SMAPE for Low: {}".format(smap_low))
            st.write("Optimal Level for Low: {} ".format(optim_level_low))
            st.write("Optimal Trend for Low: {} ".format(optim_trend_low))
            st.write("Optimal Seasonal smoothing for Low: {}".format(optim_season_low))

    elif model == 'Auto Regressive Model':
        col1, col2 = st.columns(2)
        with col1:
            p_high = st.slider("Order of High", 1, 30, 1)
        with col2:
            p_low = st.slider("Order of Low", 1, 30, 1)
        from SES import AR_model

        data_final, smap_high, smap_low = AR_model(data,horizon,p_high,p_low)
        st.line_chart(data_final[['High', 'Forecast_High', 'Low', 'Forecast_Low']])
        col1, col2 = st.columns(2)
        with col1:
            st.write("SMAPE of High: {}".format(smap_high))
        with col2:
            st.write("SMAPE of Low : {}".format(smap_low))

    elif model == 'Moving Average Model':
        col1, col2 = st.columns(2)
        with col1:
            q_high = st.slider("Order of High", 1, 30, 1)
        with col2:
            q_low = st.slider("Order of Low", 1, 30, 1)
        from SES import AR_model
        data_final, smap_high, smap_low = AR_model(data, horizon, q_high, q_low)
        st.line_chart(data_final[['High', 'Forecast_High', 'Low', 'Forecast_Low']])
        col1, col2 = st.columns(2)
        with col1:
            st.write("SMAPE of High: {}".format(smap_high))
        with col2:
            st.write("SMAPE of Low : {}".format(smap_low))

    elif model == 'ARMA Model':
        col1, col2 = st.columns(2)
        with col1:
            p_high = st.slider("Order of AR High", 1, 30, 1)
            q_high = st.slider("Order of MA High", 1, 30, 1)
        with col2:
            p_low = st.slider("Order of AR Low", 1, 30, 1)
            q_low = st.slider("Order of MA Low", 1, 30, 1)
        from SES import ARMA_model
        data_final, smap_high, smap_low = ARMA_model(data,horizon,p_high,p_low,q_high,q_low)
        st.line_chart(data_final[['High', 'Forecast_High', 'Low', 'Forecast_Low']])
        col1, col2 = st.columns(2)
        with col1:
            st.write("SMAPE of High: {}".format(smap_high))
        with col2:
            st.write("SMAPE of Low : {}".format(smap_low))

    elif model == 'ARIMA Model':
        col1, col2 = st.columns(2)
        with col1:
            p_high = st.slider("Order of AR High", 1, 30, 1)
            q_high = st.slider("Order of MA High", 1, 30, 1)
            i_high = st.slider("Order of Differencing High" , 0,10,0)
        with col2:
            p_low = st.slider("Order of AR Low", 1, 30, 1)
            q_low = st.slider("Order of MA Low", 1, 30, 1)
            i_low = st.slider("Order of Differencing Low", 0, 10, 0)
        from SES import ARIMA_model
        data_final, smap_high, smap_low = ARIMA_model(data,horizon,p_high,p_low,q_high,q_low,i_high,i_low)
        st.line_chart(data_final[['High', 'Forecast_High', 'Low', 'Forecast_Low']])
        col1, col2 = st.columns(2)
        with col1:
            st.write("SMAPE of High: {}".format(smap_high))
        with col2:
            st.write("SMAPE of Low : {}".format(smap_low))
    
    else:
        from ML_models import forecast
        data_final, smape_high, smape_low = forecast(data,horizon,model)
        st.line_chart(data_final[['High', 'Forecast_High', 'Low', 'Forecast_Low']])

        col1, col2 = st.columns(2)
        with col1:
            st.write("SMAPE of High: {}".format(smape_high))
        with col2:
            st.write("SMAPE of Low : {}".format(smape_low))

db.close()
