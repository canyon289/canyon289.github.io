Title: Hi, I'm Ravin
Date: 2016-4-21 
Slug:  index
Authors: Ravin Kumar
Status: Published
save_as: index.html 

<style type="text/css">
    /* Headers */
    h1, h2 {
        text-align: center;
    }
    h3 {
        text-align: left
    }
    h1:not(.page-title), h2, h3, h4 {
        margin-top: 2.5rem;
    }
    .action-link h3 {
        margin: auto 1rem;
    }  
    .my-work-text h3,
    .my-work-text p {
        margin: auto 0;
    }

    /* Containers */
    .about-container {
        display: flex;
        flex-direction: row;
    }
    .about-container .about-box {
        flex: 1;
        padding: 2rem;
    }
    #action-links {
        max-width: 100%;
        margin: 10px auto;
        display: flex;
        flex-wrap: wrap;
        flex-direction: column;
        justify-content: center;
    }
    .action-link, .my-work {
        display: flex;
        flex-direction: row;
    }
    @media (max-width: 768px) {
        .about-container {
            flex-direction: column;
        }
    }

    /* Box and colors */
    .action-link {
        width: 100%;
        background-color: #f4f5fb;
        -webkit-transition: all 0.15s ease;
        transition: all 0.15s ease;
    }
    .action-link, .secondary-box {
        border-radius: 5px;
        margin: 1.5%;
        padding: 15px;
    }
    .secondary-box {
        border: solid 1px #56bb92;
        min-height: 100px;
        margin-top: 1.5rem;
    }
    .action-link:hover,
    .my-work:hover {
        box-shadow: 0 0 10px #ccc;
    }
    .my-work-text {
        color: #12221d;
        margin: auto 0;
    }
    
    /* Images */
    .action-link img {
        height: 60px;
        width: 60px;
        margin: auto 0;
    }
    .my-work-img-container {
        width: 80px;
        margin: auto 20px;
    }
    .my-work img {
        margin: auto;
    }
</style>

<svg viewbox="0 0 100 100" style="opacity:12%;max-width:100px;max-height:100px; margin:40px auto;">
    <style type="text/css">
        path {
            fill: none;
            stroke: #12221D;
            stroke-width: 0.1rem;
            stroke-miterlimit: 10;
            stroke-linecap: round;
        }
        #K-triangle-1,
        #K-triangle-2 {
            stroke-dasharray: 1;
            stroke-dashoffset: 1;
            animation: dash 2s linear forwards;
        }
        #R-triangle-circle {
            stroke-dasharray: 1;
            stroke-dashoffset: 1;
            animation: dash 2.4s linear forwards;           }
        @keyframes dash {
            to {
                stroke-dashoffset: 0;
            }
        }
    </style>
    <g id="R">
        <path id="R-triangle-circle" d="M 15 42.1297 L 43.5792 91.6304 L 15 91.6304 L 15 8.3696 A 32.0984 32.0984 0 0 1 15 72.5664 Z" pathLength="1"/>
    </g>
    <g id="K">
        <path id="K-triangle-1" d="M 56.2434 58.1775 L 85 8.3696 L 56.2434 8.3696 Z" pathLength="1"/>
        <path id="K-triangle-2" d="M 56.2434 42.1297 L 85 91.6304 L 56.2434 91.6304 Z" pathLength="1"/>
    </g>
</svg>

<div class="about-container">
<!-- Left -->
    <div class="about-box">
        <h1 style="margin-top:0; text-align: left;">About Me</h1>
        <p>I am a data scientist at Google. My focus is supporting strategic decision making with data, although all my opinions here are my own. Previously, I worked at Sweetgreen and SpaceX, doing the same line of work as now but on different applications, which is using data to inform staffing strategy and rocket launch cadence.</p>
        <p>To become a better "decision" scientist, I'm currently focusing on three topics:</p>
        <ol>
            <li>Organizational influence and leadership</li>
            <li>Advanced applied mathematics, e.g. Causal Inference, Decision Theory</li>
            <li>Knowledge of business processes</li>
        </ol>
        <p>I like to share and teach the skills I've found useful from my career, whether it be here or in <a href="./blog.html">my blog</a>, on <a href="https://www.youtube.com/channel/UCX78cJQ_6JZVUWw8cj-f0uA/featured">YouTube</a>, or as part of <a href="https://www.intuitivebayes.com/">my course series</a>.</p>
        <p>If you'd prefer to have updates pushed to you, you can subscribe to my mailing list.</p>
        <p>I also contribute heavily to open source, mainly with <a href="https://arviz-devs.github.io/arviz/index.html">ArviZ</a> and <a href="https://docs.pymc.io/">PyMC</a>.</p>
        <p>I'm always happy to connect with interested folks. Feel free to reach out anytime.</p>
    </div>
<!-- Right -->
    <div class="about-box">
        <h1 style="margin-top:0; text-align: left;">My Ongoing Work</h1>
        <a href="https://github.com/canyon289/canyon289.github.io"><div class="action-link"><img src="./images/about/github.png" /><h3>My Open Source Profile</h3></div></a>
        <a href="https://www.youtube.com/channel/UCX78cJQ_6JZVUWw8cj-f0uA/featured"><div class="action-link"><img src="./images/about/youtube.png" /><h3>My YouTube Channel</h3></div></a>
        <a href="./blog.html"><div class="action-link"><img src="./images/logo/logo.png" /><h3>My Blog</h3></div></a>
        <div class="secondary-box" style="width: 100%;"> 
            <h3 style="margin-top:0;">Join my mailing list for updates</h3>
            <p>Get the latest updates on my blog posts, new YouTube series, upcoming talks, ongoing collaborations, and thoughtful discussions. You can unsubscribe at anytime.</p>
            <form class="ml-block-form" action="https://static.mailerlite.com/webforms/submit/k0j3t8" data-code="k0j3t8" method="post" target="_blank" style="height: 32px;">
                <div class="ml-form-formContent horozintalForm">
                    <div class="ml-form-horizontalRow">
                        <div class="ml-input-horizontal">
                            <div style="width:100%" class="horizontal-fields">
                                <div class="ml-field-group ml-field-email ml-validate-email ml-validate-required">
                                    <input type="email" class="form-control" data-inputmask="" name="fields[email]" placeholder="Email" autocomplete="email" aria-invalid="false">
                                </div>
                            </div>
                        </div>
                        <div class="ml-button-horizontal primary">
                            <button type="submit" class="primary" style="font-weight: 700; font-size: 14px;">Subscribe</button>
                            <button disabled="disabled" style="display:none" type="button" class="loading"> <div class="ml-form-embedSubmitLoad"></div> <span class="sr-only">Loading...</span> </button>
                        </div>
                    </div>
                </div>
                <input type="hidden" name="ml-submit" value="1" aria-invalid="false">
                <div class="ml-mobileButton-horizontal">
                    <button type="submit" class="primary" style="font-weight: 700; font-size: 14px;">Subscribe</button>
                    <button disabled="disabled" style="display:none" type="button" class="loading"> <div class="ml-form-embedSubmitLoad"></div> <span class="sr-only">Loading...</span> </button>
                </div>
                <input type="hidden" name="anticsrf" value="true" aria-invalid="false">
            </form>
        </div>
    </div>
</div>

# See my work

<div><a href="https://bayesiancomputationbook.com/welcome.html"><div class="secondary-box my-work">
    <div class="my-work-img-container"><img src="./images/about/book.jpeg" /></div>
    <div class="my-work-text">
        <h3>Bayesian Modeling and Computation in Python</h3>
        <p>I co-authored a free textbook on statistical modeling.</p>
    </div>
</div></a></div>

<div><a href="https://www.intuitivebayes.com/"><div class="secondary-box my-work">
    <div class="my-work-img-container"><img src="./images/about/course.png" /></div>
    <div class="my-work-text">
        <h3>Courses in Intuitive Statistics</h3>
        <p>I co-developed courses for professionals looking to learn applied statistics hand-on.</p>
    </div>
</div></a></div>


# Talks

### Intro to Bayesian Model Evaluation and Visualization
SciPy 2019  
[Recording](https://www.youtube.com/watch?v=bmWMdVQlzIA&E)
&nbsp;
[Code](https://github.com/canyon289/bayesian-model-evaluation)  
<br>

### PyTest for Data Scientists
PyDataLA 2018  
[Recording](https://www.youtube.com/watch?v=dY1nNtDTruE)
&nbsp;
[Code](https://github.com/canyon289/PyTestforDataSciencePyDataLA)  
<br>

### PyTest
Code Camp 2017  
_Introductory level talk meant to encourage others to use python testing by going through basic and intermediate PyTest examples._  
[Code](https://github.com/canyon289/CodeCampPytest)
&nbsp;
[Slides](https://docs.google.com/presentation/d/11A742qhUaQdtwL3IaXQGzT3lB9PfRTXOIN4SpgSbwxo/edit#slide=id.p)  
<br>
