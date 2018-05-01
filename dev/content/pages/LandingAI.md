Title: Welcome!
Date: 2016-4-21 
Slug: landingai
Authors: Ravin Kumar
Status: hidden

If you've reached this page I'm assuming you've seen my video (If not it's HereSDFS)

Everything shown is real, from my 3D printer to the CNN.
The content represents what I'm able to do, work at the intersection of
modern data methods and manufacturing.
This is also what'd I'd bring to Landing.ai along with my enthusiasm and prior experience.

If the feeling is mutual please feel free to contact me. Linkedin works well! (link on the left)


# Behind the Scenes - 23b Hackerspace 
The video was filmed in 23b hackerspace.
A hackerspace is a community space where people can use industrial tools that are unlikely 
unlikely to be available for individual use. In this manner folks can 
learn about manufacturing with hands on experience and through practical use.
For me in particular this space was particular helpful by providing a practical
space to apply what I had learned in an academic classroom.

# The CNN Recognizer
  
[https://github.com/canyon289/LandingAI](https://github.com/canyon289/LandingAI)

In the video you can see that a CNN finds the correct Camera Image from a set of
a dummy images. The project in the video was not arbitrary. I actually chose it because its very practical example end to end training pipeline for manufacturing.

I wanted the CNN to be able recognize a manufactured object with a specific message from a set of images of other objects that were similar in shape and size, but contained different text. It would have been prohibitively dollar and time expensive to manufacture and take pictures of thousands of training samples, so instead I had Python computationally generate thousands of images that approximated pictures of the real thing instead. During the image generation some random noise as added to help generalization. The results were excellent, the model trained on computationally generated images was very easily able to recognize the picture of the real thing.

This small scale example is directly relevant to industrial scale manufacturing. Making physical parts is an expensive process, and top of that digitizing reality into bits is another expensive process. This approach was published by OpenAI, but to take credit I've seen and been a part of similar efforts prior to the publish of this article (https://blog.openai.com/generalizing-from-simulation/)

At LandingAI these are the types of problems I want to help solve, not just the Artificial Intelligence bit, but all the challenges to incorporate newer data capabilities into a manufacturing business. Hopefully you found this as interesting as I did. If so I hope to hear back from you!






