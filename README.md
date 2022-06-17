<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="Images/y%20(1200%20%C3%97%20900px)%20(1200%20%C3%97%20900px).png" alt="Logo" width="240" height="180">
  </a>

  <h3 align="center">Stock Prediction ML App</h3>

  <p align="center">
    <i>
    Never, ever argue with your trading system.
    </i>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->

  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#models-used">Models Used</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>





<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

As any one of us could guess, the market is unstable and, more than often, unpredictable. For several decades researchers have toyed with time-series data to predict future values – of which the most challenging and potentially lucrative application is predicting the values of stocks for a given company. However, as expected, market change depends on many parameters of which only a bunch can be quantified, such as historical stock data, the volume of trade, current prices. Of course, fundamental factors such as a company’s intrinsic value, assets, quarterly performance, recent investments, and strategies all affect the traders’ trust in the company and thus the price of its stock. Only a few of the latter can be incorporated effectively into a mathematical model. 

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!

Use the `BLANK_README.md` to get started.

<p align="right">(<a href="#top">back to top</a>)</p>



### Models Used

Time series models are used to forecast events based on verified historical data. Common types include ARIMA, smooth-based, and moving average. Not all models will yield the same results for the same dataset, so it's critical to determine which one works best based on the individual time series.

* [Simple Exponential Smoothing](https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/README.md#simple-exponential-smoothing)
* [Double Exponential Smoothing](https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/README.md#double-exponential-smoothing)
* [Triple Exponential Smoothing](https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/README.md#triple-exponential-smoothing)
* [Auto Regressive Model](https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/README.md#auto-regressive-model)
* [Moving Average Model](https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/README.md#moving-average-model)
* [ARMA Model](https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/README.md#arma-model)
* [ARIMA Model](https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/README.md#arima-model)
* [Linear Regression](https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/README.md#linear-regression)
* [Random Forest](https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/README.md#random-forest)


<p align="right">(<a href="#top">back to top</a>)</p>




<!-- GETTING STARTED -->
## Models


### Simple Exponential Smoothing

A simple exponential smoothing is one of the simplest ways to forecast a time series. The basic idea of this model is to assume that the future will be more or less the same as the (recent) past. Thus, the only pattern that this model will learn from demand history is its level. This model is called exponential smoothing as the weight given to each demand observation is exponentially reduced.

#### Model

The underlying idea of an exponential smoothing model is that, at each period, the model will learn a bit from the most recent demand observation and remember a bit of the last forecast it did. The magic about this is that the last forecast populated by the model already included a part of the previous demand observation and a part of the previous forecast. And so forth. That means that this previous forecast includes everything the model learned so far based on demand history. The smoothing parameter (or learning rate) alpha will determine how much importance is given to the most recent demand observation.

<p align="center">
  <img src="https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/Images/1_tEim5aRYlu346TLsYja_UA.png" />
</p>

* <b>alpha</b> is a ratio (or a percentage) of how much importance the model will allocate to the most recent observation compared to the importance of demand history.
* <b>alpha d{t-1}</b> represents the previous demand observation times the learning rate. You could say that the model attaches a certain weight (alpha) to the last demand occurrence.
* <b>(1-alpha) f{t-1}</b> represents how much the model remembers from its previous forecast. Note that this is where the recursive magic happens as f{t-1} was itself defined as partially d{t-2} and f{t-2}.

<p align="right">(<a href="#top">back to top</a>)</p>

### Double Exponential Smoothing

This method is also known as Holt’s method, after Charles C. Holt and his paper from 1957. 

#### Model

It’s called double exponential smoothing because it’s based on two smoothing parameters — Alpha (for level) and Beta (for trend). The algorithm solves the primary issue of simple exponential smoothing, as now the forecasts can account for the trend in historical data. Speaking of trend, it can be either additive or multiplicative:

* <b>Additive trend</b> — trend grows linearly over time.
* <b>Multiplicative trend</b> — trend doesn’t grow linearly and shows a curvature — even a slight one.

<p align="center">
  <img src="https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/Images/1_GtUcDLKCF9-vGixEGFSFlQ.png" />
</p>

* <b>l(t)</b> is level at time t.
* <b>x(t)</b> is data value at time t.
* <b>b(t)</b> is trend at time t.
* <b>n</b> represents the number of time steps into the future. 
* <b>Alpha</b> and <b>Beta</b> are the smoothing parameters. <b>Alpha</b> is weight for the level and <b>Beta</b> is weight for the trend.
* <b>ŷ(t+n)</b> is n-step-ahead forecast, at time t.


<p align="right">(<a href="#top">back to top</a>)</p>

### Triple Exponential Smoothing

Three years later (1960), Peter R. Winters and Charles. C. Holt extended the original Holt’s method to address for seasonality. The algorithm was named after both of them — Holt-Winters’ method.

#### Model

Triple exponential smoothing is used to handle the time series data containing a seasonal component. Yet another parameter was added — Gamma — to address for the seasonal component. Just like trend, the seasonality can also be additive or multiplicative. 

<p align="center">
  <img src="https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/Images/1_LSv1WT3GuCWQdhjL_gNWBw.png" />
</p>

* <b>l(t)</b> is level at time t.
* <b>x(t)</b> is data value at time t.
* <b>b(t)</b> is trend at time t.
* <b>c(t)</b> is seasonality at time t.
* <b>n</b> represents the number of time steps into the future. 
* <b>Alpha</b> (Data smoothing factor. The range is 0 < α <1.), <b>Beta</b> (Trend smoothing factor. The range is 0 < β < 1.) and <b>Gamma</b> (Seasonal change smoothing factor. The range is 0 < γ <1.) are the smoothing parameters. <b>Alpha</b> is weight for the level, <b>Beta</b> is weight for the trend and <b>Gamma</b> is weight for the seasonality.
* <b>ŷ(t+n)</b> is n-step-ahead forecast, at time t.

<p align="right">(<a href="#top">back to top</a>)</p>

### Auto Regressive Model

In a multiple regression model, we forecast the variable of interest using a linear combination of predictors. In an autoregression model, we forecast the variable of interest using a linear combination of past values of the variable. The term autoregression indicates that it is a regression of the variable against itself.

#### Model

Autoregressive models are remarkably flexible at handling a wide range of different time series patterns. We normally restrict autoregressive models to stationary data, in which case some constraints on the values of the parameters are required.

<p align="center">
  <img src="https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/Images/autoc.JPG" />
</p>

* <b>ε(t)</b> is white noise. This is like a multiple regression but with lagged values of <b>y(t)</b> as predictors. We refer to this as an <b>AR(p) model</b>, an autoregressive model of order <b>p</b>.

<p align="right">(<a href="#top">back to top</a>)</p>

### Moving Average Model

Rather than using past values of the forecast variable in a regression, a moving average model uses past forecast errors in a regression-like model.

#### Model

It is a time series model that accounts for very short-run autocorrelation. It basically states that the next observation is the mean of every past observation.

<p align="center">
  <img src="https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/Images/1_oI1OSoT-9UlLZ09456LD-g.png" />
</p>

<p align="right">(<a href="#top">back to top</a>)</p>

### ARMA Model

An ARMA model, or Autoregressive Moving Average model, is used to describe weakly stationary stochastic time series in terms of two polynomials. The first of these polynomials is for autoregression, the second for the moving average.

#### Model

Often this model is referred to as the <b>ARMA(p,q) model</b>; where:

<p align="center">
  <img src="https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/Images/arma.jpeg" />
</p>

* p is the order of the autoregressive polynomial.

* q is the order of the moving average polynomial.

<p align="right">(<a href="#top">back to top</a>)</p>

### ARIMA Model

ARIMA, short for ‘Auto Regressive Integrated Moving Average’ is actually a class of models that ‘explains’ a given time series based on its own past values, that is, its own lags and the lagged forecast errors, so that equation can be used to forecast future values.

#### Model

<p align="center">
  <img src="https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/Images/Equation-4-min.png" />
</p>

* Predicted Yt = Constant + Linear combination Lags of Y (upto p lags) + Linear Combination of Lagged forecast errors (upto q lags)

* The objective, therefore, is to identify the values of p, d and q. .

<p align="right">(<a href="#top">back to top</a>)</p>

### Linear Regression

Linear regression analysis is used to predict the value of a variable based on the value of another variable. The variable you want to predict is called the dependent variable. The variable you are using to predict the other variable's value is called the independent variable.

#### Model

Ordinary least squares (OLS) is a method to quantify the evaluation of the different regression lines. According to OLS, we should choose the regression line that minimizes the sum of the squares of the differences between the observed dependent variable and the predicted dependent variable.

<p align="center">
  <img src="https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/Images/1_cfD_EOOIo6sG1Thch6QeTQ.png" />
</p>

We can find a line that best fits the observed data according to the evaluation standard of OLS. A general format of the line is:

<p align="center">
  <img src="https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/Images/11_BsIOb5DT_4L6ZOqsyK7M7A.png" />
</p>

* Here, μᵢ is the residual term that is the part of yᵢ that cannot be explained by xᵢ.

<p align="right">(<a href="#top">back to top</a>)</p>

### Random Forest

Random Forest is a popular machine learning algorithm that belongs to the supervised learning technique. It is an ensemble learning method, constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes (classification) or mean/average prediction (regression) of the individual trees. It can be used for both Classification and Regression problems in ML. However, it can also be used in time series forecasting, both univariate and multivariate dataset by creating lag variables and seasonal component variables manually.

<p align="right">(<a href="#top">back to top</a>)</p>

