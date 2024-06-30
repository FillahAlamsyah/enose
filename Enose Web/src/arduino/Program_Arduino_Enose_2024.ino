//Include the library
#include <MQUnifiedsensor.h>

/************************Hardware Related Macros************************************/
#define         Board          ("Arduino Mega 2560")
#define         MQ2_Pin        A13
#define         MQ3_Pin        A2
#define         MQ4_Pin        A9
#define         MQ5_Pin        A14
#define         MQ6_Pin        A7
#define         MQ7_Pin        A12
#define         MQ8_Pin        A11
#define         MQ9_Pin        A8
#define         MQ131_Pin      A1
#define         MQ135_Pin      A15
#define         MQ136_Pin      A6
#define         MQ137_Pin      A5
#define         TGS813_Pin     A4
#define         TGS822_Pin     A10
#define         TGS2600_Pin    A3
#define         TGS2611_Pin    A0

/************************ Ratio Clean Air *************************
******************************************************************/
#define         MQ2_RatioCleanAir        9.7431763878509     //✅
#define         MQ3_RatioCleanAir        59.86711485         //✅
#define         MQ4_RatioCleanAir        4.43668733097861    //✅
#define         MQ5_RatioCleanAir        9.07775665399239    //✅
#define         MQ6_RatioCleanAir        9.7978507682058     //✅
#define         MQ7_RatioCleanAir        25.9245848804407    //✅
#define         MQ8_RatioCleanAir        70.4442602636407    //✅
#define         MQ9_RatioCleanAir        9.89172120959352    //✅
#define         MQ131_RatioCleanAir      12.3541085904841    //✅
#define         MQ135_RatioCleanAir      3.60631995560172    //✅
#define         MQ136_RatioCleanAir      3.56633705835168    //✅
#define         MQ137_RatioCleanAir      3.5                 //✅
#define         TGS813_RatioCleanAir     4.90920576959119    //✅
#define         TGS822_RatioCleanAir     17.0482967846829    //✅
#define         TGS2600_RatioCleanAir    1                   //✅
#define         TGS2611_RatioCleanAir    8.50188876408541    //✅

/***********************Software Related Macros************************************/
#define         ADC_Bit_Resolution        (10) // 10 bit ADC 
#define         Voltage_Resolution        (5) // Volt resolution to calc the voltage
#define         Type                      ("MQ") //Board used
#define         RegressionMethod          (1)

/*************************** Gas Array ****************************
  FORMAT :  float GasH2[2] = {a,b};       // Nama Sensor
  Diambil dari Datasheet setiap sensor
*******************************************************************/
float GasPropana[2]   = {637.15, -2.203};        // Sensor MQ2--✅
float GasHexana[2]    = {22.795, -0.357};         // Sensor MQ3--✅
float GasLPG2[2]     = {3816.8, -3.122};      // Sensor MQ4--✅ lpg oy
float GasCO[2]        = {999498, -6.474};        // Sensor MQ5--✅
float GasCH4[2]       = {2201, -2.522};          // Sensor MQ6--✅
float GasH2[2]        = {68.238, -1.354};        // Sensor MQ7--✅
float GasAlcohol[2]   = {48685, -1.689};         // Sensor MQ8--✅
float GasLPG[2]       = {1056.1, -2.355};        // Sensor MQ9--✅
float GasNoX[2]       = {469.5, -2.155};        // Sensor MQ131--✅
float GasCL2[2]       = {48.017, -1.191};        // Sensor MQ131--✅
float GasO3[2]        = {24.338, -1.1};        // Sensor MQ131--✅
float GasCO2[2]       = {111.84, -2.902};        // Sensor MQ135--✅
float GasToluena_MQ135[2] = {44.977, -3.437};        // Sensor MQ135--✅
float GasH2S[2]       = {37.332, -3.52};         // Sensor MQ136--✅
float GasAmonia[2]    = {34.464, -3.4};       // Sensor MQ137--✅ {-0.243,0.323};
float GasEtanol[2]    = {1321.6, -1.683};        // Sensor TGS813--✅
float GasBenzena[2]   = {342.05, -1.512};        // Sensor TGS822--✅
float GasAseton[2]    = {272.19, -1.141};           // Sensor TGS822--✅
float GasMetana[2]   = {1.6734, -10.66};         // Sensor TGS2600--✅
float GasButana[2]    = {3407.6, -1.708};         // Sensor TGS2611--✅

/*************************** Class Sensor ****************************
*******************************************************************/
MQUnifiedsensor MQ2(            Board, Voltage_Resolution, ADC_Bit_Resolution, MQ2_Pin, Type);
MQUnifiedsensor MQ3(            Board, Voltage_Resolution, ADC_Bit_Resolution, MQ3_Pin, Type);
MQUnifiedsensor MQ4(            Board, Voltage_Resolution, ADC_Bit_Resolution, MQ4_Pin, Type);
MQUnifiedsensor MQ5(            Board, Voltage_Resolution, ADC_Bit_Resolution, MQ5_Pin, Type);
MQUnifiedsensor MQ6(            Board, Voltage_Resolution, ADC_Bit_Resolution, MQ6_Pin, Type);
MQUnifiedsensor MQ7(            Board, Voltage_Resolution, ADC_Bit_Resolution, MQ7_Pin, Type);
MQUnifiedsensor MQ8(            Board, Voltage_Resolution, ADC_Bit_Resolution, MQ8_Pin, Type);
MQUnifiedsensor MQ9(            Board, Voltage_Resolution, ADC_Bit_Resolution, MQ9_Pin, Type);
MQUnifiedsensor MQ131_NoX(      Board, Voltage_Resolution, ADC_Bit_Resolution, MQ131_Pin, Type);
MQUnifiedsensor MQ131_CL2(      Board, Voltage_Resolution, ADC_Bit_Resolution, MQ131_Pin, Type);
MQUnifiedsensor MQ131_O3(       Board, Voltage_Resolution, ADC_Bit_Resolution, MQ131_Pin, Type);
MQUnifiedsensor MQ135_CO2(      Board, Voltage_Resolution, ADC_Bit_Resolution, MQ135_Pin, Type);
MQUnifiedsensor MQ135_Toluena(  Board, Voltage_Resolution, ADC_Bit_Resolution, MQ135_Pin, Type);
MQUnifiedsensor MQ136(          Board, Voltage_Resolution, ADC_Bit_Resolution, MQ136_Pin, Type);
MQUnifiedsensor MQ137(          Board, Voltage_Resolution, ADC_Bit_Resolution, MQ137_Pin, Type);
MQUnifiedsensor TGS813(         Board, Voltage_Resolution, ADC_Bit_Resolution, TGS813_Pin, Type);
MQUnifiedsensor TGS822_Benzena( Board, Voltage_Resolution, ADC_Bit_Resolution, TGS822_Pin, Type);
MQUnifiedsensor TGS822_Aseton(  Board, Voltage_Resolution, ADC_Bit_Resolution, TGS822_Pin, Type);
MQUnifiedsensor TGS2600(        Board, Voltage_Resolution, ADC_Bit_Resolution, TGS2600_Pin, Type);
MQUnifiedsensor TGS2611(        Board, Voltage_Resolution, ADC_Bit_Resolution, TGS2611_Pin, Type);

/*************************** Debug Print ****************************
*******************************************************************/
String separator = "\t";

void setup() {
  Serial.begin(9600);

  MQ2.setRegressionMethod(RegressionMethod);
  MQ2.setA(GasPropana[0]); MQ2.setB(GasPropana[1]);
  MQ2.setR0(calibrate(MQ2, MQ2_RatioCleanAir, "MQ2"));
  MQ2.init();

  MQ3.setRegressionMethod(RegressionMethod);
  MQ3.setA(GasHexana[0]); MQ3.setB(GasHexana[1]);
  MQ3.setR0(calibrate(MQ3, MQ3_RatioCleanAir, "MQ3"));
  MQ3.init(); 

  MQ4.setRegressionMethod(RegressionMethod);
  MQ4.setA(GasLPG2[0]); MQ4.setB(GasLPG2[1]);
  MQ4.setR0(calibrate(MQ4,MQ4_RatioCleanAir, "MQ4"));
  MQ4.init(); 

  MQ5.setRegressionMethod(RegressionMethod);
  MQ5.setA(GasCO[0]); MQ5.setB(GasCO[1]);
  MQ5.setR0(calibrate(MQ5, MQ5_RatioCleanAir, "MQ5"));
  MQ5.init(); 

  MQ6.setRegressionMethod(RegressionMethod);
  MQ6.setA(GasCH4[0]); MQ6.setB(GasCH4[1]);
  MQ6.setR0(calibrate(MQ6, MQ6_RatioCleanAir, "MQ6"));
  MQ6.init(); 

  MQ7.setRegressionMethod(RegressionMethod);
  MQ7.setA(GasH2[0]); MQ7.setB(GasH2[1]);
  MQ7.setR0(calibrate(MQ7, MQ7_RatioCleanAir, "MQ7"));
  MQ7.init(); 

  MQ8.setRegressionMethod(RegressionMethod);
  MQ8.setA(GasAlcohol[0]); MQ8.setB(GasAlcohol[1]);
  MQ8.setR0(calibrate(MQ8, MQ8_RatioCleanAir, "MQ8"));
  MQ8.init(); 

  MQ9.setRegressionMethod(RegressionMethod);
  MQ9.setA(GasLPG[0]); MQ9.setB(GasLPG[1]);
  MQ9.setR0(calibrate(MQ9,MQ9_RatioCleanAir, "MQ9"));
  MQ9.init(); 

  MQ131_NoX.setRegressionMethod(RegressionMethod);
  MQ131_NoX.setA(GasNoX[0]); MQ131_NoX.setB(GasNoX[1]);
  MQ131_NoX.setR0(calibrate(MQ131_NoX, MQ131_RatioCleanAir, "MQ131"));
  MQ131_NoX.init(); 

  MQ131_CL2.setRegressionMethod(RegressionMethod);
  MQ131_CL2.setA(GasCL2[0]); MQ131_CL2.setB(GasCL2[1]);
  MQ131_CL2.setR0(calibrate(MQ131_CL2, MQ131_RatioCleanAir, "MQ131"));
  MQ131_CL2.init();

  MQ131_O3.setRegressionMethod(RegressionMethod);
  MQ131_O3.setA(GasO3[0]); MQ131_O3.setB(GasO3[1]);
  MQ131_O3.setR0(calibrate(MQ131_O3, MQ131_RatioCleanAir, "MQ131"));
  MQ131_O3.init();

  MQ135_CO2.setRegressionMethod(RegressionMethod);
  MQ135_CO2.setA(GasCO2[0]); MQ135_CO2.setB(GasCO2[1]);
  MQ135_CO2.setR0(calibrate(MQ135_CO2,MQ135_RatioCleanAir, "MQ135"));
  MQ135_CO2.init(); 

  MQ135_Toluena.setRegressionMethod(RegressionMethod);
  MQ135_Toluena.setA(GasToluena_MQ135[0]); MQ135_Toluena.setB(GasToluena_MQ135[1]);
  MQ135_Toluena.setR0(calibrate(MQ135_Toluena,MQ135_RatioCleanAir, "MQ135"));
  MQ135_Toluena.init(); 

  MQ136.setRegressionMethod(RegressionMethod);
  MQ136.setA(GasH2S[0]); MQ136.setB(GasH2S[1]);
  MQ136.setR0(calibrate(MQ136,MQ136_RatioCleanAir, "MQ136"));
  MQ136.init(); 

  MQ137.setRegressionMethod(RegressionMethod);
  MQ137.setA(GasAmonia[0]); MQ137.setB(GasAmonia[1]);
  MQ137.setR0(calibrate(MQ137,MQ137_RatioCleanAir, "MQ137"));
  MQ137.init(); 

  TGS813.setRegressionMethod(RegressionMethod);
  TGS813.setA(GasEtanol[0]); TGS813.setB(GasEtanol[1]);
  TGS813.setR0(calibrate(TGS813,TGS813_RatioCleanAir, "TGS813"));
  TGS813.init(); 

  TGS822_Benzena.setRegressionMethod(RegressionMethod);
  TGS822_Benzena.setA(GasBenzena[0]); TGS822_Benzena.setB(GasBenzena[1]);
  TGS822_Benzena.setR0(calibrate(TGS822_Benzena,TGS822_RatioCleanAir, "TGS822"));
  TGS822_Benzena.init(); 

  TGS822_Aseton.setRegressionMethod(RegressionMethod);
  TGS822_Aseton.setA(GasAseton[0]); TGS822_Aseton.setB(GasAseton[1]);
  TGS822_Aseton.setR0(calibrate(TGS822_Aseton,TGS822_RatioCleanAir, "TGS822"));
  TGS822_Aseton.init(); 

  TGS2600.setRegressionMethod(RegressionMethod);
  TGS2600.setA(GasMetana[0]); TGS2600.setB(GasMetana[1]);TGS2600.setRL(10);
  TGS2600.setR0(calibrate(TGS2600,TGS2600_RatioCleanAir, "TGS2600"));
  TGS2600.init();
  //TGS2602.setRL(0.45);

  TGS2611.setRegressionMethod(RegressionMethod);
  TGS2611.setA(GasButana[0]); TGS2611.setB(GasButana[1]);
  TGS2611.setR0(calibrate(TGS2611,TGS2611_RatioCleanAir, "TGS2611"));
  TGS2611.init(); 
  delay(500);
}

void loop() {
  MQ2.update();MQ3.update();MQ4.update();MQ5.update();
  MQ6.update();MQ7.update();MQ8.update();MQ9.update();
  MQ131_NoX.update();MQ131_CL2.update();MQ131_O3.update();
  MQ135_CO2.update();MQ135_Toluena.update();
  MQ136.update();MQ137.update();TGS813.update();
  TGS822_Benzena.update();TGS822_Aseton.update();
  TGS2600.update();TGS2611.update();

  boolean ppm = true;
  if (ppm){
    Print_ppm();
  }else{
    Print_ADC();
  }
  delay(100);
}
void Print_ppm(){
  Serial.print(MQ2.readSensor());             Serial.print(" "); //Propana
  Serial.print(MQ3.readSensor());             Serial.print(" "); //Hexana
  Serial.print(MQ4.readSensor()/10);             Serial.print(" "); //LPG2
  Serial.print(MQ5.readSensor());             Serial.print(" "); //CO
  Serial.print(MQ6.readSensor());             Serial.print(" "); //CH4
  Serial.print(MQ7.readSensor());             Serial.print(" "); //H2
  Serial.print(MQ8.readSensor()/10);             Serial.print(" "); //Alcohol
  Serial.print(MQ9.readSensor());             Serial.print(" "); //LPG
  Serial.print(MQ131_NoX.readSensor());       Serial.print(" "); //NoX
  Serial.print(MQ131_CL2.readSensor());       Serial.print(" "); //CL2
  Serial.print(MQ131_O3.readSensor());        Serial.print(" "); //O3
  Serial.print(MQ135_CO2.readSensor());       Serial.print(" "); //CO2
  Serial.print(MQ135_Toluena.readSensor());   Serial.print(" "); //Toluena
  Serial.print(MQ136.readSensor());           Serial.print(" "); //H2S
  Serial.print(MQ137.readSensor());           Serial.print(" "); //Amonia
  Serial.print(TGS813.readSensor()/10);          Serial.print(" "); //Etanol
  Serial.print(TGS822_Benzena.readSensor());  Serial.print(" "); //Benzena
  Serial.print(TGS822_Aseton.readSensor());   Serial.print(" "); //Aseton
  Serial.print(TGS2611.readSensor()/10);         Serial.print(" "); //Butana
  Serial.println(TGS2600.readSensor());                          //CH4
}

void Print_ADC(){
  Serial.print(analogRead(MQ2_Pin));       Serial.print(" ");
  Serial.print(analogRead(MQ3_Pin));       Serial.print(" ");
  Serial.print(analogRead(MQ4_Pin));       Serial.print(" ");
  Serial.print(analogRead(MQ5_Pin));       Serial.print(" ");
  Serial.print(analogRead(MQ6_Pin));       Serial.print(" ");
  Serial.print(analogRead(MQ7_Pin));       Serial.print(" ");
  Serial.print(analogRead(MQ8_Pin));       Serial.print(" ");
  Serial.print(analogRead(MQ9_Pin));       Serial.print(" ");
  Serial.print(analogRead(MQ131_Pin));     Serial.print(" ");
  Serial.print(analogRead(MQ135_Pin));     Serial.print(" ");
  Serial.print(analogRead(MQ136_Pin));     Serial.print(" ");
  Serial.print(analogRead(MQ137_Pin));     Serial.print(" ");
  Serial.print(analogRead(TGS813_Pin));    Serial.print(" ");
  Serial.print(analogRead(TGS822_Pin));    Serial.print(" ");
  Serial.print(analogRead(TGS2600_Pin));   Serial.print(" ");
  Serial.println(analogRead(TGS2611_Pin));
}

float calibrate(MQUnifiedsensor MQ, float ratio, String sensor){
  float calcR0 = 0;
  int n = 20;
  for(int i = 1; i<=n; i ++){
    MQ.update(); // Update data, the arduino will read the voltage from the analog pin
   calcR0 += MQ.calibrate(ratio);//Serial.print("");
  }
  calcR0 = calcR0/n; //Serial.print(sensor);Serial.print("\t"); Serial.println(calcR0);
  if(isinf(calcR0)) {Serial.println("Warning: Conection issue, R0 is infinite (Open circuit detected) please check your wiring and supply"); while(1);}
  if(calcR0 == 0){Serial.println("Warning: Conection issue found, R0 is zero (Analog pin shorts to ground) please check your wiring and supply"); while(1);}
  return calcR0;
}
