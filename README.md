# Cell-Stretching-Machine

{add final prototype here} 

## Part of Senior Capstone Project for the Mechanical and Aerospace Department at University of California, San Diego  
## Contributors: Kaustubh Kanagalekar, Alexander Haken, Sheen Shaji, Justin Dang, Jason Liu

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

{insert picture of knee tissues} 

This project is sponsored by Dr. Peter Chen and Erik Dorthe from the Shiley Center for Orthopedic Research and Education, who are seeking a system capable of applying tensile loading (stretching) to tendon tissues and compressive loading (squeezing) to meniscus tissues. These mechanical forces are critical in promoting proper growth by mimicking the natural physiological conditions tissues experience in the human body. Specifically, these forces help cells create a proper extracellular matrix, a foundational structure necessary for healthy and functional tissue growth. Tissue samples will be immersed in a nutrient-rich solution for approximately two weeks to sustain cell activity during mechanical stimulation.

---

## Objectives
The sponsors have requested the development of a new biomechanical culture system capable of applying both tensile and compressive forces to soft tissue samples, specifically tendons and meniscus tissues. Tensile and compressive applications will not be concurrent within one experiment, but rather respective to the experiment being run. This system must be fully functional within a standard cell incubator environment, operating at approximately 37˚C with over 90 % relative humidity. To meet the experimental and biological needs, the system must satisfy the following requirements:

- Deliver forces up to 20 N on tissue samples.
- Operate reliably within the incubator conditions mentioned above.
- Apply cyclic loading at frequencies up to 1 Hz or lower.
- Achieve up to 10 percent strain on samples.
- Include an automated or user-friendly nutrient feeding system to maintain cell viability over extended periods.
- Be sterilizable, with components that are either autoclavable or compatible with chemical sterilization.
- Feature modular, removable clamp designs that are compatible with various tissue geometries and can support both tensile and compressive loading.

---

## System Overview / Methodology
{add picture of final CAD design} 

The final design of the Biomechanical Culture Reactor, as seen in the figure above, integrates six main subsystems: the SMAC actuator, custom lift plate, linear rail carriage, modular clamp interface, load cell assembly, and the petri-dish nutrient tray. All components are mounted on a precision-machined aluminum baseplate designed for high stiffness and compatibility with incubator environments. The SMAC actuator provides programmable tension and compression to the mounted tissue specimens, with cyclic strain control up to 10% at 1 Hz. This motion is transferred through a linear rail carriage system for smooth and low-friction actuation.

Specimens are held in place using modular clamps—interchangeable between compression and tension modes—mounted onto a removable lift plate that enables easy extraction of the culture system for media replacement. The quick-release fasteners ensure minimal disruption during removal. A 5kg ATO load cell provides real-time feedback, ensuring applied forces stay within the desired range. The final design prioritizes modularity, sterilization compatibility (via aluminum and stainless steel components), and scalability for future automation.

### Key Components 
1. **SMAC Actuator**  
   {add image of SMAC Actuator}  
   > ### Overview  
   The purpose of the actuator is to provide a mechanism to deliver tensile and compressive forces to the specimen samples. Some choices that were considered include piezoelectric motors, stepper motors, and linear actuators, however the SMAC actuator was chosen because of the ease of procurement and performance specifications.
   
   > ### Functional Requirements  
   >> * The actuator shall provide up to 20 N of force.  
   >> * The actuator shall run in 1 Hz cycles.  
   >> * The actuator shall contain a resolution of 1µm.

   > ### Justification  
   The actuator provided an exceptional positional resolution of 10 µm, exceeding the precision required for reliably achieving the necessary strain increments in the biological samples. Its high-accuracy linear positioning ensured repeatability, crucial for maintaining consistent mechanical stimuli during extended experimental periods.

   > Secondly, the SMAC actuator delivered consistent, backlash-free performance due to its unique moving-coil design. The absence of backlash in the actuator eliminated concerns about drift and unintended motion, which are critical for maintaining the integrity and repeatability of tests that last over multiple weeks.
   
   > Furthermore, the actuator effectively operated at the required cyclic frequency of 1 Hz without loss of accuracy or mechanical instability. The robustness of SMAC actuator's design offered reliable cyclic operation, crucial for mimicking the physiological conditions necessary for tissue growth and maturation.

2. **Tension Clamps**  
   {add image of tension clamps}  
   > ### Overview  
   The clamps used in this design serve as a holder for the specimen during experiments. The clamps enable the specimen to stretch and compress, allowing them to grow during the course of the experiment. There are two types of clamp design: one for tension, the other for compression. This presents information for tension clamps. The specimen size used for tensile experiments is roughly 20 mm by 5 mm. 
   
   > ### Functional Requirements  
   >> * The clamps shall be easily sterilizable (thus made out of metal).  
   >> * The clamps shall be modular (can be replaced with other types of clamps easily).  
   >> * The clamps shall be able to hold the samples throughout the experiment without causing them to slip. 

   > ### Justification  
   This clamp version incorporated modularity through the use of T-slots and T-nuts, enabling quick interchangeability between different clamp types. This feature was especially beneficial for the project since the system needed to accommodate both tensile and compressive samples with differing geometries and dimensions. The modular interface allowed for faster setup and teardown between experiments, reduced the risk of sample mishandling, and provided long-term flexibility for future experimental configurations.
  > In terms of mechanical performance, this iteration also maintained a strong and secure grip on the specimen throughout the loading cycles. This was crucial, as slippage during stretching or compression could compromise experimental data and hinder proper tissue development. The design’s ability to maintain a consistent clamping force under cyclic mechanical loading improved the reliability of results and ensured that strain measurements remained accurate throughout the testing period.

3. **Linear Rail Design**  
   {add image of linear rails}  
   > ### Overview  
   The design utilizes a gantry to translate the linear motion of the SMAC actuator to the array of clamps holding the specimens. This enables the specimen to receive tensile and compressive forces that aid in their growth and development.  
   > ### Functional Requirements  
   >> * The rails shall exhibit minimal friction and wobble when in operation.  
   > ### Justification  
   The rail and carriage system from McMaster-Carr was chosen because it exhibited extremely low friction during inspection and seemed extremely durable.

4. **Quick Release Fasteners**  
   {add image for quick release}  
   > ### Overview  
   The user needs to be able to quickly separate key parts of the assembly in order to perform manual refeeding of the nutrient medium. Parts to be quickly released include the plates holding the slots for clamps as well as load cell and linear actuator from the gantry. The quick release fasteners are an alternative to using traditional fasteners such as bolts and nuts which may create a large delay in nutrient refeeding and provide extra parts that may be easily misplaced.  
   > ### Functional Requirements  
   >> * Secure Connection: Must firmly fasten aluminum plates and stainless steel blocks without unintended detachment during operation.  
   >> * Tool-Free Operation: Should allow engagement and release by hand (e.g., quarter-turn or button press), without requiring screwdrivers, wrenches, or Allen keys.  
   >> * Sterilization Compatibility: Must be constructed entirely from corrosion-resistant metals (stainless steel or anodized aluminum) to withstand alcohol wiping and incubator conditions (37°C, 90% humidity).  
   >> * Compact Form Factor: Must have a low-profile design to fit within spatial constraints inside the reactor’s petri dish platform and avoid interfering with adjacent components.  
   >> * Repeatable Reliability: Should be durable for repeated fastening cycles (20+ uses) without significant wear or degradation of locking performance.

   > ### Justification  
   After comparing multiple fastening mechanisms, fixtures from the IMAO company were selected. More specifically, the IMAO Quarter Turn Fasteners were chosen as the final solution due to their optimal balance of performance, reliability, and integration ease. These fasteners provided a secure mechanical connection between key components—specifically, the lift plate, clamp carriage, actuator mount, and load cell interface—while maintaining a compact profile suitable for the limited space within the incubator-compatible reactor base.  
   The tool-free quarter-turn locking mechanism allowed users to detach and reattach parts in under 10 seconds, a major improvement over traditional fasteners which often required several minutes of careful disassembly. This quick-release functionality significantly reduced downtime during nutrient refeeding and helped maintain sterility by minimizing exposure time. In addition, their stainless steel construction ensured that they were compatible with frequent alcohol-based sterilization and resistant to corrosion from prolonged exposure to humidity.

---

## Implementation Details

### Hardware
Many of the components seen in the CAD and the prototype were machined. The lift plate was CNC milled from a stock of 3/8 in flat aluminum. The clamps, quick release slider plate, rigid 8020 mount, and other metal pieces were manufactured using water jet cutting from 1/2 in aluminum stock. The clamps were water jet cut from a stock of 1/2 in aluminum and attached to a T-slot bar using M 7.5 T-nuts for secure attachment. They were assembled with M 4.5 screws. These clamps were knurled to aid gripping during specimen loading. 

The quick release slider plate, rigid 8020 mount, and other metal pieces were faced off to match the required height dimensions (~5.5 mm ± 0.2 mm) for seamless connection with the fasteners. Overall assembly involved attaching each component using standard screws (M 2, M 3, M 4, etc.) and bolts, with dial indicators used to ensure alignment precision.

### Software
The control system was developed in **LabVIEW**. A custom VI interface was created to enable the actuator to move specific distances based on user inputs for frequency, sample length, and number of cycles. The load cell, rated at 5 kg with 0.3% accuracy, was connected via a load amplifier for data acquisition and visualization. Load and timestamp data were logged as CSV files.

**Operation guide:**  
- Connect system to PC via RS232  
- Open the LabVIEW VI  
- Input the number of samples, set zero, and configure strain, frequency, and cycles  
- Run the experiment  
- Download the CSV data for analysis

---

## Results

### Data
Two validation tests were conducted:

- **Test 1:** Dynamic loading of a 20 mm sample at 0.2 Hz yielded a maximum force of **18 N**, close to the 20 N target.  
- **Test 2:** Friction measurement indicated an internal system friction of approximately **0.65 N**.

### Evaluation
The system successfully met force and frequency specifications, with low friction observed. Load data confirmed the actuator's effective transfer of force and stability during cyclic operation. The minimal phase lag and slip indicate reliable clamp engagement, and the low friction baseline supports its suitability for biological experiments.

---

## Challenges Faced
- Material selection issues for clamps and components due to sterilization and humid conditions, leading to redesigns with stainless steel and anodized aluminum.  
- Friction in linear carriage affected load measurement accuracy, prompting sourcing of higher-precision components.  
- Ensuring sterilization compatibility required modifications to avoid plastics and favor metals.  
- The iterative design process was essential to optimize alignment, component security, and durability.

---

## Future Improvements
- Enhance rail stiffness and machining tolerances to improve low-force measurement accuracy.  
- Develop quicker, more intuitive clamp and fastener systems for ease of specimen exchange.  
- Create a user-friendly GUI with real-time monitoring and feedback control.  
- Incorporate force/displacement sensors for closed-loop control.  
- Use materials optimized for repeated sterilization cycles.  
- Add safety features like overload alarms and automatic shutdown protocols.

---

## Conclusion
This project successfully developed a modular, reliable biomechanical culture reactor capable of applying controlled tensile and compressive forces within an incubator. The prototype demonstrated effective force output, low friction, and sterilization compatibility, providing a platform for orthopedic tissue engineering research. Further biological testing and automation enhancements will advance its applicability toward clinical and research use.

---

#### Acknowledgements
- SCORE Lab – Shiley Center for Orthopedic Research and Education  
- Dr. Peter Chen  
- Erik Dorthé  

**Department of Mechanical and Aerospace Engineering, UC San Diego**  
- Professor Nathan Delson  
- Jackie Chen  
- Thomas Chalfant  
- Stephen Mercsak  

**UCSD Makerspace**  
- David Lesser  
- Mark Liu

