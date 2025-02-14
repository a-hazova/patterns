const Converter = (()=>{
    const FOOT = 30.48
    const INCH = 2.54 
    const MILE = 1609.34

    return {
        inchesToCentimeters: (inches) => inches * INCH,
        feetToMeters: (feet) => feet * FOOT,
        milesToKilometers: (miles) => miles * MILE
    }

})()

export default Converter;

console.log(Converter.inchesToCentimeters(12)) 