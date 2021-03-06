# ClusterFuzzLite for CI development

For the ambitious learners following this tutorial, we would like to provide resources and explain how you can integrate ClusterFuzzLite with your Atheris fuzz targets to create a fuzzing based CI workflow. CI based fuzzing is extremely valuable for software projects of all sizes.

This section of the tutorial will need to be completed in your own repository locally outside of the Katacoda environment. For this reason we are designating this as a challenge section and is not required for completion of the learning outcomes. However, we highly recommend you read through the sources we provide in case you decide to use ClusterFuzzLite on a project of your own.

To setup ClusterFuzzLite, specifically with Atheris for Python fuzzing:

1. Create Fuzz targets 
2. Install Docker
3. Clone the oss-fuzz repo 

Next you will need to integrate ClusterFuzzLite with your project:

This includes creating three files in a .clusterfuzzlite directory in the root of your project: project.yaml, Dockerfile, build.sh

1. All that is necessary in project.yaml is a line defining the language as python <br />

2. The Docker file should specify base-builder-python. Then "You should simply clone the project, set a WORKDIR, and copy any necessary files, or install any project-specific dependencies here as you normally would." 

3. "For Python projects, build.sh does need some more significant modifications over normal projects. The following is an annotated example build script, explaining why each step is necessary and when they can be omitted."

For detailed instructions on the build integration see [https://google.github.io/clusterfuzzlite/build-integration/](https://google.github.io/clusterfuzzlite/build-integration/)

We also recommend directly following the Python template given in the documentation: [https://google.github.io/clusterfuzzlite//build-integration/python-lang/](https://google.github.io/clusterfuzzlite//build-integration/python-lang/)


4. Finally your ClusterFuzzLite workflow can be integrated through GitHub Actions.  <br />

This is another simple step with ClusterFuzzLite and the file can be directly used from the documentation once the repository has been set up. 

For further instructions such as how to set up batch fuzzing or corpus pruning refer to the documentation https://google.github.io/clusterfuzzlite/running-clusterfuzzlite/github-actions/