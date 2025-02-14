interface personalData {
    firstName: string;
    lastName: string;
    age: number;
    id: number;
    address: string;
}



class Passport {
    data: personalData
    private static instance: Passport;

    private constructor(data: personalData) {
        this.data = data;
    }

    static getInstance(data?: personalData): Passport  {
        if (this.instance) return this.instance
        if (data) this.instance = new Passport(data)
        return this.instance
    }

    changeFirstName(newName: string) {
        this.data.firstName = newName
    }
}

const myData = {
    firstName: "Nastja",
    lastName: "Khazova",
    age: 27,
    id: 58781,
    address: "Taganrog",
}

const anotherData = {
    firstName: "",
    lastName: "",
    age: 11,
    id: 2,
    address: "",
}

const myPassport = Passport.getInstance(myData)
const myPassport2 = Passport.getInstance()
myPassport.changeFirstName('Anastasia')