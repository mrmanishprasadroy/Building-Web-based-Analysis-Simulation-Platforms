Building Web-base Analysis & simulation Platforms with react, Flask, Celery, Bokeh, and Numpy
Description What use is analytical code if it can't be integrated into a business workflow to solve real problems? This tutorial is about integrating analytical work into a real production system that can be used by business users. It focuses on building a web-based platform for managing long-running analytical code and presenting results in a convenient format, using cutting-edge combination of tools.

Abstract The purpose of this stack is to be able to rapidly create web-based environments for users to interact with the results of analytical and simulation processes (without needing to retrain one's self as a web programmer!)

This tutorial is composed of the following pieces:

building a simple simulation using Numpy. For the purposes of this tutorial, we model a very simple Monte Carlo simulation with a number of user-controllable, tweakable algorithm inputs and model parameters. The simulation is chosen to be simple enough to present and code quickly. The purpose of this tutorial is not building Monte Carlo simulations but packaging them into lightweight production systems.

Celery for launching and managing the above simulation jobs. This tutorial will not cover all aspects of Celery. It will merely show how the tool can be used as a job management system.

Flask as a very thin JSON API layer. The tutorial will make use of Flask plugins for quickly building JSON APIs. This is the thinnest and least interesting component of the tutorial and won't be covered in great depth.

React + Redux for a slick, simple single-page app. Attendees are expected to be least familiar with Javascript and the React ecosystem. The tutorial will spend a fair amount of time on this component, and will cover setting up build environment using Babel (for JSX transpilation) and Gulp as a build system.

Bokeh for presenting graphical results from the simulation. This component may be cut based on time considerations.
