
# Cell-Stretching-Machine-

![Final Prototype](assets/Misc/FinalAssembly.jpg)

## Part of Senior Capstone Project for the Mechanical and Aerospace Department at University of California, San Diego 
### Contributors: Kaustubh Kanagalekar, Alexander Haken, Sheen Shaji, Justin Dang, Jason Liu 

---

## Table of Contents
- [Abstract](#abstract)
- [Motivation](#motivation)
- [Objectives](#objectives)
- [System Overview / Methodology](#system-overview--methodology)
- [Implementation Details](#implementation-details)
- [Results](#results)
- [Challenges Faced](#challenges-faced)
- [Future Improvements](#future-improvements)
- [Conclusion](#conclusion)

---

## Abstract 
  Musculoskeletal tissue repair such as that of tendons and meniscus play a vital role in recovery from numerous sports-related injuries and in improving the quality of life amongst the elderly population. Orthopedic scientists are constantly researching novel techniques for growing artificial cells on tissues that can replace or supplement traditional methods for musculoskeletal tissue repair. Dr. Peter Chen and Erik Dorthé, scientists from the Shiley Center of Orthopedic Research and Education researching on orthopedic repair methods, would like to see a biomechanical culture reactor (also referred to as a “cell stretcher” or "cell stretching machine") device that can provide tensile and compressive forces on tissues to artificially foster their growth. This device shall provide these types of forces, operate reliably within an incubator environment at approximately 37°C and 90% relative humidity, and feature an effective system for refilling the nutrient solution necessary for sustained tissue development. The current design approach integrates a precise pushing and pulling mechanism driven by a SMAC (Smart Motor Actuator Company) linear actuator capable of high accuracy motion control, a low-friction linear gantry constructed from stainless steel rails to minimize wobble and enhance stability, and modular clamps made from sterilizable stainless steel, ensuring a secure grip on the tissue samples. Final results of the cell stretcher system indicate low coulombic friction of 0.7 N and operating force of 18 N, closely achieving the required force output. The future implications of this device hold great potential for regenerative medicine and biofabrication with further refinements and tests. 

---

## Motivation
  The motivation behind developing a biomechanical culture reactor lies in addressing the clinical need for effective regeneration of musculoskeletal tissues, particularly tendon and meniscus tissues. These tissues are commonly damaged in sports-related injuries or age-related conditions such as knee osteoarthritis, often requiring surgical interventions like tendon repair or knee replacement. The culture reactor aids in tissue regeneration by applying controlled mechanical stimulation—stretching or compressing the tissues—in a laboratory setting, replicating natural conditions to promote healthy tissue growth.

![Image of Tendons](assets/Misc/knee.png)

  This project is sponsored by Dr. Peter Chen and Erik Dorthe from the Shiley Center for Orthopedic Research and Education, who are seeking a system capable of applying tensile loading (stretching) to tendon tissues and compressive loading (squeezing) to meniscus tissues. These mechanical forces are critical in promoting proper growth by mimicking the natural physiological conditions tissues experience in the human body. Specifically, these forces help cells create a proper extracellular matrix, a foundational structure necessary for healthy and functional tissue growth. Tissue samples will be immersed in a nutrient-rich solution for approximately two weeks to sustain cell activity during mechanical stimulation.

---

## Objectives
  The sponsors have requested the development of a new biomechanical culture system capable of applying both tensile and compressive forces to soft tissue samples, specifically tendons and meniscus tissues. Tensile and compressive applications will not be concurrent within one experiment, but rather respective to the experiment being run. This system must be fully functional within a standard cell incubator environment, operating at approximately 37˚C with over 90 % relative humidity. To meet the experimental and biological needs, the system must satisfy the following requirements:


* Deliver forces up to 20 N on tissue samples.
* Operate reliably within the incubator conditions mentioned above.
* Apply cyclic loading at frequencies up to 1 Hz or lower.
* Achieve up to 10 percent strain on samples.
* Include an automated or user-friendly nutrient feeding system to maintain cell viability over extended periods.
* Be sterilizable, with components that are either autoclavable or compatible with chemical sterilization.
* Feature modular, removable clamp designs that are compatible with various tissue geometries and can support both tensile and compressive loading.

---

## System Overview / Methodology

![Final CAD Prototype](assets/Misc/CADOverview.png)

  The final design of the Biomechanical Culture Reactor, as seen in the figure above, integrates six main subsystems: the SMAC actuator, custom lift plate, linear rail carriage, modular clamp interface, load cell assembly, and the petri-dish nutrient tray. All components are mounted on a precision-machined aluminum baseplate designed for high stiffness and compatibility with incubator environments. The SMAC actuator provides programmable tension and compression to the mounted tissue specimens, with cyclic strain control up to 10% at 1 Hz. This motion is transferred through a linear rail carriage system for smooth and low-friction actuation.

  Specimens are held in place using modular clamps—interchangeable between compression and tension modes—mounted onto a removable lift plate that enables easy extraction of the culture system for media replacement. The quick-release fasteners ensure minimal disruption during removal. A 5kg ATO load cell provides real-time feedback, ensuring applied forces stay within the desired range. The final design prioritizes modularity, sterilization compatibility (via aluminum and stainless steel components), and scalability for future automation.

### Key Components 
---

#### 1. SMAC Actuator

![SMAC Actuator](assets/Misc/SMACpic.png)

#### Overview  
The purpose of the actuator is to provide a mechanism to deliver tensile and compressive forces to the specimen samples. Some choices that were considered include piezoelectric motors, stepper motors, and linear actuators; however, the SMAC actuator was chosen due to ease of procurement and performance specifications.

#### Functional Requirements  
- The actuator shall provide up to 20 N of force.  
- The actuator shall run in 1 Hz cycles.  
- The actuator shall contain a resolution of 1 µm.

#### Justification  
The actuator provided an exceptional positional resolution of 10 µm, exceeding the precision required for reliably achieving the necessary strain increments in the biological samples. Its high-accuracy linear positioning ensured repeatability, crucial for maintaining consistent mechanical stimuli during extended experimental periods.

Secondly, the SMAC actuator delivered consistent, backlash-free performance due to its unique moving-coil design. The absence of backlash eliminated concerns about drift and unintended motion, which are critical for maintaining the integrity and repeatability of tests over multiple weeks.

Furthermore, the actuator operated at the required cyclic frequency of 1 Hz without loss of accuracy or mechanical instability. Its robust design offered reliable cyclic operation, crucial for mimicking the physiological conditions necessary for tissue growth and maturation.

---

#### 2. Tension Clamps

![Tension Clamps](assets/Misc/Clamps.jpg)

#### Overview  
The clamps used in this design serve as holders for the specimen during experiments. They enable the specimen to stretch and compress, facilitating growth during the experiment. Two clamp designs exist: one for tension and another for compression. This section describes the tension clamps, used for specimens roughly 20 mm by 5 mm.

#### Functional Requirements  
- The clamps shall be easily sterilizable (thus made out of metal).  
- The clamps shall be modular (interchangeable with other types).  
- The clamps shall securely hold samples without slippage.

#### Justification  
This clamp version incorporated modularity through T-slots and T-nuts, enabling quick interchangeability between different clamp types. This feature was beneficial for accommodating both tensile and compressive samples of varying geometries.

Mechanically, this iteration maintained a strong grip on the specimen throughout loading cycles. Slippage during stretching or compression could compromise data, so consistent clamping improved experimental reliability and ensured accurate strain measurements.

---

#### 3. Linear Rail Design

![Rails and Carriages](assets/Misc/Rails.png)

#### Overview  
The design utilizes a gantry to translate the linear motion of the SMAC actuator to the array of clamps holding the specimens. This enables the specimen to receive tensile and compressive forces to aid growth and development.

#### Functional Requirements  
- The rails shall exhibit minimal friction and wobble during operation.

#### Justification  
The rail and carriage system from McMaster-Carr was chosen for its extremely low friction and robust construction. This ensured reliable motion transmission, improving the accuracy and consistency of force application during testing.

---

#### 4. Quick Release Fasteners

![Quick Release Fasteners](assets/Misc/QuickRelease.png)

#### Overview  
The user must quickly separate parts of the assembly to manually refeed nutrient medium. Detachable parts include the clamp plate, load cell, and actuator mount. Quick-release fasteners offer an efficient alternative to bolts and nuts, which slow down access and pose a risk of losing small parts.

#### Functional Requirements  
- **Secure Connection**: Must fasten plates and blocks without detachment.  
- **Tool-Free Operation**: Must engage and release by hand.  
- **Sterilization Compatibility**: Must be corrosion-resistant and sterilizable.  
- **Compact Form Factor**: Must fit within spatial constraints.  
- **Repeatable Reliability**: Must withstand 20+ cycles of fastening/unfastening.

#### Justification  
Fixtures from IMAO, specifically the Quarter Turn Fasteners, were selected for their optimal balance of performance, reliability, and compact design. They enabled fast, tool-free removal and reattachment of key parts in under 10 seconds.

This reduced downtime during refeeding and minimized contamination risk. Their stainless-steel construction supported repeated alcohol sterilization and durability under humid incubator conditions.

---

## Implementation Details

### Hardware
  Many of the components seen in the CAD and the prototype were machined. The lift plate was CNC milled using a stock of 3/8 in flat aluminum. The clamps, quick release slider plate, rigid 8020 mount, and other metal pieces were manufactured using water jet. The clamps were water jet from a stock of 1/2 in aluminum and attached to a T-slot bar using T-nuts (M 7.5) for a secure attachment. They were attached together using M 4.5 screws. These clamps were also knurled to aid the gripping mechanism when loading up a specimen. 

  The quick release slider plate, rigid 8020 mount and the other metal pieces were also water jet from the stock of 1/2 in aluminum; they were later faced off to match the correct height dimensions as required by the quick release fasteners to connect seamlessly. They were faced to a height of 5.5 mm +/- 0.2 mm. 
  The overall assembly consisted of attaching each of the components (machined and bought) using standard screws (such as M 3, M 4, M 2, etc) and bolts. Dial indicators were used in the assembly of the rails to ensure alignment accuracy. 

### Software
  The software aspect of this project was powered by LabView. A LabView script/interface was developed that would enable the actuator to move a certain distance. The user could input a desired frequency rate, the sample length, and the number of desired cycles, and the LabView program would run according.  

  In addition, a load cell was attached to the end of the actuator's shaft to read the force outputs exerted by the actuator. This load cell was a tension and compression load cell from ATO rated for 5 kg, with an accuracy of 0.3 % full scale range. A load cell amplifier was attached to the load cell for easy load data logging and visualization. 
  The LabView program was configured to log a timestamp of the corresponding load cell value for every experimental run. This log was saved as a csv file that could be extracted for data comparison and viualization. 

  Here is a brief guide on operating the LabView program- 
  > It is imperative that the system is connected to a host PC/laptop using a RS232 connector. In order to run the system, one should download the LabVIEW interface and perform the following tasks 

   * Download and open the custom VI LabVIEW code (found in the code section of the [website](https://sites.google.com/eng.ucsd.edu/mae156b-2025spring-team02))
   * Write the number of samples to be tested, 
   * Setting the “zero”
   * Programming a desired strain, frequency, and number of cycles
   * Run the program
A csv file with the load data and timestamps is saved after each run which can be downloaded for data collection and plotting purposes. 


## Results
### Data
For the final design iteration, the following tests were conducted: two initial validation tests were conducted under different operating conditions. These tests were designed to verify the functionality of the SMAC actuator under load and to assess the level of internal system friction in the absence of a specimen. The first test consisted of dynamic loading of a 20 mm sample at 0.2 Hz cycles.  The load cell output during this test is shown in the figure below- 

![Data 1](assets/Misc/Data2.png)
  As seen in the above figure, the maximum force obtained was 18 N, thus closely matching the required force output of 20 N from the actuator. 

For the second test, inertial system friction was measured. The result of this test can be seen in Figure 4.2.4. 

![Data 2](assets/Misc/Data1.png)
    As seen in the above figure, the maximum friction measured was roughly 0.65 N. 
 
### Evaluation
  The results of the final design performance tests confirmed that the mechanical design was capable of meeting the majority of the functional force and frequency requirements. With applied forces meeting the requirements of 20 N and measuring an extremely low frictional force, the final system indicates that it can meet and exceed the requirements set forth at the beginning of the project while being as efficient as possible. 

  The lack of force decay or phase lag across cycles further indicates that the clamps held the specimen firmly without slipping, even under high-cycle loading. This suggests that the mechanical interfaces between actuator, load cell, and specimen were securely integrated. With no specimen inserted, the actuator's back-and-forth motion produced minimal reactive force, with the load cell detecting a maximum friction force of approximately 0.65 N for the design. 

  The performance difference between the two tests can be interpreted in terms of system efficiency. Under load, most of the actuator’s output was effectively transferred to the specimen, whereas under no-load conditions, internal mechanical friction became the dominant force captured by the load cell. This difference validates the team’s approach to minimizing friction through component selection and alignment strategies.

  Furthermore, the results imply that any small load measurements recorded in actual tissue tests—especially in the sub-2 N range—must be interpreted carefully, as they may include minor contributions from system friction. However, given the low friction baseline, the load cell readings for most biological samples (which are expected to fall in the 5–15 N range) will remain reliable.

  ![Operational Movie](assets/Misc/Operation.MOV)

# Challenges Faced
  Over the course of this project, the team developed not only a functional prototype but also a deeper understanding of the interdisciplinary challenges involved in biomedical device development. One of the most important lessons was the necessity of iterative prototyping. Initial clamp designs, although theoretically sound, failed under real-world incubator conditions due to inadequate material selection. This prompted a redesign using stainless steel and anodized aluminum to ensure durability, chemical resistance, and sterilizability.

  Another major insight was the significant impact of friction on mechanical performance. Even minor frictional forces introduced during carriage movement were found to skew load cell readings, affecting measurement accuracy. This led to a focus on sourcing precision linear components and refining the gantry alignment.

  Sterilization requirements also influenced system architecture more than initially anticipated. While 3D-printed plastics offered quick iteration early on, they proved unsuitable for repeated sterilization, resulting in delays and the need for mid-project reengineering of several subsystems. The importance of defining sterilization compatibility early in the design phase became evident.

# Future Improvements 
  Based on the testing outcomes and system performance analysis, several design improvements are recommended for future iterations of the biomechanical culture reactor. First, while the current gantry and linear rail system effectively minimized friction, further enhancements in alignment accuracy and rail stiffness could yield even more precise load cell readings, particularly during low-force experiments. Improved machining tolerances and the addition of anti-backlash features may help reduce unwanted mechanical resistance.

  The modularity of the system should also be enhanced. The implementation of more intuitive quick-release mechanisms and clamp-swapping features would streamline the process of specimen replacement and nutrient refeeding. Incorporating alignment pins or integrated connection guides would further reduce assembly error and setup time.

On the software side, although LabVIEW provided a workable interface for basic control, future development of a more user-friendly graphical user interface (GUI) could benefit operators, particularly for real-time monitoring and feedback adjustments. A closed-loop control system incorporating force or displacement sensors would also improve experimental consistency by allowing automatic compensation for mechanical drift or sample variability.

  Material selection should continue to prioritize sterilization compatibility. Components that contact the culture environment, such as clamps and fasteners, must withstand repeated autoclaving or chemical sterilization cycles without degradation. Future parts may benefit from being designed explicitly for ISO 17665 sterilization compliance.

Finally, as the platform evolves toward clinical research applications, integration of redundant sensing and self-check protocols would enhance reliability. This includes features like fail-safe locking mechanisms or force-limit alerts to prevent accidental overload or sample damage during long-duration testing.

# Conclusion
  This project successfully developed a functional and modular biomechanical culture reactor capable of applying controlled tensile and compressive forces to biological specimens. Through iterative design, testing, and refinement, the team produced a system that satisfies key requirements for force output, modularity, sterilizability, and low-friction operation. The device demonstrated reliable performance across test conditions and offered a platform for future biological research focused on orthopedic repair and tissue engineering.

Beyond the technical accomplishments, the project highlighted the importance of multidisciplinary collaboration, rigorous standards adherence, and iterative learning in engineering practice. The system represents a promising step toward scalable, cost-effective platforms for soft tissue research and holds the potential to inform future innovations in regenerative medicine and biofabrication.

Continued development, including expanded testing with living cells and integration of closed-loop control systems, will be necessary to transition the reactor from a proof-of-concept to a research-grade or clinical tool. Nonetheless, the current results provide a strong foundation for both academic exploration and potential translational application.

![Final Assembly ](assets/Misc/FinalAssembly2.jpg)

Please check out additional [documents](assets/Presentation%20and%20Report/MAE%20156B%20Final%20Report-2.pdf), [visuals](assets/Presentation%20and%20Report/Biomechanical%20Culture%20Reactor%20Poster%2012.57.51.pptx.pdf), and [website](https://sites.google.com/eng.ucsd.edu/mae156b-2025spring-team02) here!
 
 #### Acknowledgements
 SCORE Lab – Shiley Center for Orthopedic Research and Education
 
  Dr. Peter Chen
  
  Erik Dorthé

  
Department of Mechanical and Aerospace Engineering, University of California San Diego

Professor Nathan Delson

Jackie Chen

Thomas Chalfant

Stephen Mercsak


UCSD Makerspace

David Lesser

Mark Liu
