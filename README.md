<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Stock Prediction ML App</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
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
</details>




<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

There are many great README templates available on GitHub; however, I didn't find one that really suited my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!

Use the `BLANK_README.md` to get started.

<p align="right">(<a href="#top">back to top</a>)</p>



### Models Used

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Simple Exponential Smoothing](https://nextjs.org/)
* [Holt Model](https://reactjs.org/)
* [Holt-Winter Model](https://vuejs.org/)
* [Auto Regressive Model](https://angular.io/)
* [Moving Average Model](https://svelte.dev/)
* [ARMA Model](https://laravel.com)
* [ARIMA Model](https://getbootstrap.com)
* [Auto ARIMA](https://jquery.com)
* [Linear Regression](https://jquery.com)
* [Random Forest](https://jquery.com)
* [Gradient Boosting](https://jquery.com)
* [Support Vector Machines](https://jquery.com)

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- GETTING STARTED -->
## Models

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

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


### Double Exponential Smoothing

This method is also known as Holt’s method, after Charles C. Holt and his paper from 1957. It’s called double exponential smoothing because it’s based on two smoothing parameters — Alpha (for level) and Beta (for trend). The algorithm solves the primary issue of simple exponential smoothing, as now the forecasts can account for the trend in historical data.

#### Model

The underlying idea of an exponential smoothing model is that, at each period, the model will learn a bit from the most recent demand observation and remember a bit of the last forecast it did. The magic about this is that the last forecast populated by the model already included a part of the previous demand observation and a part of the previous forecast. And so forth. That means that this previous forecast includes everything the model learned so far based on demand history. The smoothing parameter (or learning rate) alpha will determine how much importance is given to the most recent demand observation.

<p align="center">
  <img src="https://github.com/somanyadav/Stock-Prediction-ML-App/blob/main/Images/1_GtUcDLKCF9-vGixEGFSFlQ.png" />
</p>

* <b>alpha</b> is a ratio (or a percentage) of how much importance the model will allocate to the most recent observation compared to the importance of demand history.
* <b>alpha d{t-1}</b> represents the previous demand observation times the learning rate. You could say that the model attaches a certain weight (alpha) to the last demand occurrence.
* <b>(1-alpha) f{t-1}</b> represents how much the model remembers from its previous forecast. Note that this is where the recursive magic happens as f{t-1} was itself defined as partially d{t-2} and f{t-2}.


<p align="right">(<a href="#top">back to top</a>)</p>




