Title: Hi, I'm Ravin
Date: 2016-4-21 
Slug:  index
Authors: Ravin Kumar
Status: Published
save_as: index.html 

<!-- End MailerLite Universal -->

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
        <p>I am a researcher at Google Deepmind. My focus for the last decade has been applied generative models. I previously bespoke probabilistic Bayesian model at organizations such as SpaceX. Most recently I've worked on LLMs such as Gemini and Gemma.
        </p>
        <p>At Google I contributed both to products such as <a href="https://notebooklm.google.com"> NotebookLM </a> and <a href="https://deepmind.google/models/project-mariner/"> Project Mariner </a>. You can find my work on <a href="https://scholar.google.com/citations?user=Oq99ddEAAAAJ&hl=en"> Google Scholar </a> <a href="./blog.html">my blog</a>, on <a href="https://www.youtube.com/channel/UCX78cJQ_6JZVUWw8cj-f0uA/live">YouTube channel</a>, or my text books. </p>
        <p>I also contribute heavily to open source, mainly with <a href="https://arviz-devs.github.io/arviz/index.html">ArviZ</a> and <a href="https://docs.pymc.io/">PyMC</a>.
        I'm always happy to connect with interested folks. Feel free to reach out anytime.</p>
    </div>
<!-- Right -->
    <div class="about-box">
        <h1 style="margin-top:0; text-align: left;">Some Highlights</h1>
        <a href="https://github.com/canyon289/"><div class="action-link"><img src="./images/about/github.png" /><h3>My Open Source Profile</h3></div></a>
        <a href="https://www.youtube.com/channel/UCX78cJQ_6JZVUWw8cj-f0uA/live"><div class="action-link"><img src="./images/about/youtube.png" /><h3>My YouTube Channel</h3></div></a>
        <a href="./blog.html"><div class="action-link"><img src="./images/logo/logo.png" /><h3>My Blog</h3></div></a>
        <!-- Mailerlite Form -->
        <!-- <div class="secondary-box" style="width: 100%;"> 
            <h3 style="margin-top:0;">Join my mailing list for updates</h3>
            <p>Get the latest updates on my blog posts, new YouTube series, upcoming talks, ongoing collaborations, and thoughtful discussions. You can unsubscribe at anytime.</p> -->
        <!-- <div class="ml-embedded" data-form="j1X8Q9"></div> -->
        </div>
    </div>
</div>

# See my work
<div><a href="https://ravinkumar.com/GenAiGuidebook/book_intro.html"><div class="secondary-box my-work">
    <div class="my-work-img-container"><img src="./images/about/GenaIGuidebook.png"/></div>
    <div class="my-work-text">
        <h3>A guidebook to Generative AI</h3>
        <p>There's a lot going on in GenAI these days. This guidebook helps you find your way.</p>
    </div>
</div></a></div>

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


<!-- # Other Resources

<br>

* [Talk] [SciPy 2019: Intro to Bayesian Model Evaluation and Visualization](https://www.youtube.com/watch?v=bmWMdVQlzIA&E) ([Code](https://github.com/canyon289/bayesian-model-evaluation))

* [Talk] [PyDataLA 2018: PyTest for Data Scientists](https://www.youtube.com/watch?v=dY1nNtDTruE) ([Code](https://github.com/canyon289/PyTestforDataSciencePyDataLA))

* [Talk] [Code Camp 2017: Introduction to PyTest](https://docs.google.com/presentation/d/11A742qhUaQdtwL3IaXQGzT3lB9PfRTXOIN4SpgSbwxo/edit#slide=id.p) ([Code](https://github.com/canyon289/CodeCampPytest)) -->

