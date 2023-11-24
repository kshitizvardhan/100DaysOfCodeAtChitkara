function HouseKeeper(name, age, exp, interests, langs){
        this.name=name;
        this.age=age;
        this.exp=exp;
        this.interests=interests;
        this.langs=langs;
        this.clean= function(){
            alert("Cleaning in Progress!!. Kindly Wait")
        }
    }
var houseKeeper1= new HouseKeeper("Timmy", 25, "5+ Years of experience at ABC Hotel",["Cleaning rooms","Washing"],["English","French"])
