
## Generic sensor interaction code

This code provides a reference implementation for integrating Raspberry Pi with multiple sensor APIs. 

The main code is readsensor.py which continuously reads from a sensor and outputs the readings to a specified display. From the Raspberry Pi terminal, type:

```
python readsensor.py mpu|lsm|dummy [print|plotly]
# brackets "[]" mean optional parameters; type without brackets
```
Choose a sensor from:
* mpu (MPU6050)
* lsm (LSM9DS0) 
* dummy (random generator for testing)

Choose a display from:
* print (print to text output, this is the default if blank)
* plotly (send to plot.ly)
* matplot (send to matplot)

The code structure is organized as follows:

![Code structure](https://yuml.me/diagram/plain;dir:LR/class/[readsensor]-%3E[%3C%3Cdisplay%3E%3E],%20[%3C%3Cdisplay%3E%3E]%5E-.-[printOut],%20[%3C%3Cdisplay%3E%3E]%5E-.-[plotlyOut],%20[%3C%3Cdisplay%3E%3E]%5E-.-[matplotOut],%20[readsensor]-%3E[%3C%3Csensorapi%3E%3E],%20[%3C%3Csensorapi%3E%3E]%5E-.-[dummysensor],%20[%3C%3Csensorapi%3E%3E]%5E-.-[mpu6050api],%20[%3C%3Csensorapi%3E%3E]%5E-.-[lsm9ds0api])

<!--- 
Original code passed to yuml.me:
https://yuml.me/diagram/plain;dir:LR/class/[readsensor]->[<<display>>], [<<display>>]^-.-[printOut], [<<display>>]^-.-[plotlyOut], [<<display>>]^-.-[matplotOut], [readsensor]->[<<sensorapi>>], [<<sensorapi>>]^-.-[dummysensor], [<<sensorapi>>]^-.-[mpu6050api], [<<sensorapi>>]^-.-[lsm9ds0api] 
--->

Note that sensorapi and display are just placeholders representing the real modules.



