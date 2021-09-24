import { useState, useEffect } from "react";
import React from "react";
import BeverageList from "../components/Beverage";
import { axiosInstance } from "../utils/axiosInstance";

const Vendomatic = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [beverages, setBeverages] = useState([]);
  const [coins, setCoins] = useState(0);
  const [text, setText] = useState("");

  const insertCoinHandler = (coin) => {
    axiosInstance
      .put("/", { coin })
      .then((response) => response.headers)
      .then(
        (data) => setCoins(data["x-coins"]),
        (error) => console.log(error)
      );
  };
  const retrieveCoins = () => {
    axiosInstance
      .delete("/")
      .then((response) => response.headers)
      .then(
        (data) => {
          setText(`${data["x-coins"]} coins retrieved`);
          setCoins(0);
        },
        (error) => console.log(error)
      );
  };

  useEffect(() => {
    setIsLoading(true);

    axiosInstance
      .get("/inventory/")
      .then((response) => response.data)
      .then(
        (data) => setBeverages(data),
        (error) => console.log(error)
      );

    setIsLoading(false);
  }, [coins]);

  return (
    <>
      {!isLoading && (
        <>
          <BeverageList
            items={beverages}
            setCoins={setCoins}
            setText={setText}
          />
          <h5 style={{ margin: "2%" }}>
            Current credit: {coins} quarter coins
          </h5>
          <h5 style={{ margin: "2%" }}>{text}</h5>
          <button
            className="btn btn-success"
            style={{ margin: "2%" }}
            onClick={() => insertCoinHandler(1)}
          >
            Insert Quarter Coin
          </button>
          <button className="btn btn-dark" onClick={() => retrieveCoins()}>
            Get Coins
          </button>
        </>
      )}
    </>
  );
};

export default Vendomatic;
