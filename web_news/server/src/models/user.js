module.export  = (sequalize, DataTypes) =>
    sequalize.define('User', {
        username: {
            type: DataTypes.STRING,
            unique: true 
        },

        email: {
            type: DataTypes.STRING,
            unique: true
        },

        password: {
            type:DataTypes.STRING
        }
    })