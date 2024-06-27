<a name="readme-top"></a>
<!-- HEADER -->
<br>
<br>
<br>
<div align="center">
  <a href="https://hardsploit.io">
    <img src="https://github.com/serma-safety-security/hardsploit-gui/assets/139353343/fe2b42d6-d817-4e27-99eb-7aa0d5dfe22f" alt="Hardsploit" width=550 height=77>

  </a>

  <h3 align="center">
    The essential security auditing tool for Internet of Things devices you'll need in your toolbox </h3>
    <br>
    <br>
    <hr>
  </div>
  <br>
  <div align="center">
    <img src="https://github.com/serma-safety-security/hardsploit-gui/assets/139353343/27e4db6d-98cf-4aae-9527-f133fa3bbfe6" alt="Board hardsploit" height="250">

  </div>
  <br>

<!-- TABLE OF CONTENTS -->
<div display="flex">
  <h2>Table of contents</h2>
    <ol>
      <li>
        <a href="#about">About the project</a>
      </li>
      <li>
        <a href="#getting-started">Getting Started</a>
        <ul>
          <li><a href="#prerequisites">Prerequisites</a></li>
          <li><a href="#installation">Installation</a></li>
        </ul>
      </li>
      <li>
        <a href="#create-your-project">Create your own Hardsploit project</a>
        <ul>
          <li><a href="#ihg">Install the Harsploit API</a></li>
          <li><a href="#iha">Install the Harsploit GUI</a></li>
          <li><a href="#sh">Start Harsploit</a></li>
        </ul>
      </li>
      <li><a href="#migration">Migration guide</a></li>
      <li><a href="#tech-used">Technologies used</a></li>
      <li><a href="#license">License</a></li>
    </ol>
</div>
<br><br>

<!-- ABOUT THE PROJECT -->
<a name="about"></a>
<div>
  <table>
    <tr>
      <td>
        <h2>About the project</h2>
        <p>Hardsploit is an innovative hardware security testing platform designed to aid security researchers, engineers, and auditors in analyzing and evaluating the security of hardware devices.</p>
        <p>Featuring a modular design, Hardsploit supports various interfaces like JTAG, SPI, I2C, and UART, allowing for extensive hardware testing and reverse engineering.</p>
        <div align="center"><img src="https://github.com/serma-safety-security/hardsploit-gui/assets/139353343/5db214c1-114f-4e84-8d0b-0e792068805a" width="300"></div>
        <div>
          <div>
            <h4>Main security audit functions:</h4>
            <ul>
              <li><Strong>Sniffer</Strong> (Real-time communication monitoring)</li>
              <li><Strong>Scanner</Strong> (Automatic detection of JTAG, SPI, I2C, and UART interfaces on target devices.)</li>
              <li><Strong>Injection</Strong> (Data injection to test device responses.)</li>
              <li><Strong>Memory dumping</Strong> (Extracting the contents of a chip memory)</li>
              <li><Strong>...</Strong></li>
            </ul>
            <h4>Features:</h4>
            <ul>
              <li><Strong>Advanced Firmware Analysis:</Strong> Detects and analyzes vulnerabilities in firmware.</li>
              <li><Strong>Hardware Exploit Tools:</Strong> Tools to exploit detected vulnerabilities.</li>
              <li><Strong>Secure Firmware Update:</Strong> Updates firmware while ensuring security and integrity.</li>
              <li><Strong>Enhanced User Interface:</Strong> More intuitive and interactive interface.</li>
              <li><Strong>...</Strong></li>
            </ul>
            <h4>Supported communication protocols:</h4>
            <ul>
              <li><Strong>UART</Strong> (Universal Asynchronous Receiver-Transmitter)</li>
              <li><Strong>SPI</Strong> (Serial Peripheral Interface)</li>
              <li><Strong>I2C</Strong> (Inter-Integrated Circuit)</li>
              <li><Strong>JTAG</Strong> (Joint Test Action Group)</li>
              <li><Strong>SWD</Strong> (Serial Wire Debug)</li>
              <li><Strong>NRF24L01 (Work in progress)</Strong></li>
              <li><Strong>...</Strong></li>
            </ul>
          </div>
          <br>
          <div align="center" >
            <img src="https://github.com/serma-safety-security/hardsploit-gui/assets/139353343/d6212525-a5b3-4313-8ea3-567add4ffcb3" width="500">

          </div>
        </div>
      </td>
    </tr>
  </table>
</div>
<br><br>

<!-- GETTING STARTED -->
<a name="getting-started"></a>
<div>
  <h2>Getting Started</h2>
  <p>This guide will help you quickly get started with Hardsploit, covering the necessary prerequisites and installation steps.</p>
  <a name="prerequisites"></a>
  <h3>Pre-requisites</h3>
  <p> To be able to start using Hardsploit, make sure that you have the following prerequisites installed:</p>
  <ul>
    <li>Python v3.9 or later</li>
    <li>A Linux machine (tested on Ubuntu, Kali and Raspberry Pi OS)</li>
  </ul>
  <a name="installation"></a>
  <h3>Installation</h3>
  <ol>
    <li>
      <p>Install the Hardsploit GUI.</p>
      <code>pip install hardsploit-gui</code>
    </li>
    <br>
    <li>
      <p>That's all! Now you can start hardsploit with the following command.</p>
      <code>harsploit</code>
    </li>
  </ol>
  <br>
  <a name="create-your-project"></a>
  <h2>Create your own Hardsploit project</h2>
  <p>If you want to make your Hardsploit more personal, here is the guide.</p>
  <h3>Pre-requisites</h3>
  <p> To be able to develope your project, make sure that you have the following prerequisites:</p>
  <ul>
    <li>Python v3.9 or later</li>
    <li>A Linux machine (tested on Ubuntu, Kali, Debian and Raspberry Pi OS)</li>
    <li>A virtual environment</li>
  </ul>
  <ol>
    <a name="iha"></a>
    <li>
      <h3>Install the Hardsploit api!</h3>
      <ol>
        <li>
          <p>Clone <a href="">Hardsploit Api</a>.</p>
          <code>git clone "https://gitlabs3.serma.com/serma_s3_iec/produits-s3/hardsploitv1-python/hardsploit-gui.git"</code>
        </li>
        <br>
        <li>
          <p>Go in the cloned repository (Here, you can modifie the api)</p>
          <code>cd "Path/To/Hardsploit</code>
        </li>
        <br>
        <li>
          <p>Build the API</p>
          <code>poetry build</code>
        </li>
        <br>
        <li>
          <p>Install the API</p>
          <code>poetry install</code>
        </li>
        <br>
      </ol>
    </li>
    <a name="ihg"></a>
    <li>
      <h3>Install the Hardsploit gui</h3>
      <ol>
        <li>
          <p>Clone <a href="">Hardsploit GUI</a>.</p>
          <code>git clone ""</code>
        </li>
        <br>
        <li>
          <p>Go in the cloned repository (Here, you can modifie the GUI)</p>
          <code>cd Path/to/hardsploit-gui</code>
        </li>
        <br>
        <li>
          <p>Build the GUI</p>
          <code>poetry build</code>
        </li>
        <br>
        <li>
          <p>Install the GUI</p>
          <code>poetry install</code>
        </li>
      </ol>
    </li>
    <br>
    <a name="sh"></a>
    <li>
      <h3>Start Hardsploit</h3>
      <code>poetry run hardsploit</code>
    </li>
  </ol>
</div>
<br><br>

<!-- MIGRATION GUIDE -->
<a name="migration"></a>
<div>
  <h2>Migration guide</h2>
  <img src="./Images/migration.png" alt="">
  <ol>
    <li>Click on the import button (or ctrl + V)</li>
    <li>Choose the old database (.sqlite3 file)</li>
    <li>Then press "Import"</li>
  </ol>
  <p>This import button can also be use to import saved component, commands or both. Just select a .json file</p>
  <p>To save multiple components, click on the export button.</p>
</div>
<br><br>

<!-- TECHNOLOGIES USED-->
<a name="tech-used"></a>
<div>
  <h2>Technologies used</h2>
  <p>This project has been developed using the following technologies:</p>
  <ul>
    <li><Strong>Python</Strong> (Programming language used for project development.)</li>
    <li><Strong>PySide6</Strong> (Python framework for developing graphical user interfaces (GUI).)</li>
    <li><Strong>Poetry</Strong> (Dependency management tool for Python projects.)</li>
    <li><Strong>Peewee</Strong> (A small, expressive ORM (Object-Relational Mapping) library for Python.)</li>
  </ul>
</div>
<br><br>

<!-- LICENSE -->
<a name="license"></a>
<div>
  <h2>License</h2>
  <p>Hardsploit is licensed under *LGPLv3*. See the <a href="http://test.fr">LICENSE</a> file for more information.</p>
</div>

