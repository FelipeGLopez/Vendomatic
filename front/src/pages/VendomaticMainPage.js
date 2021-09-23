import { useState, useEffect } from "react";
import React from "react";
import BeverageList from "../components/Beverage";
import axios from "axios";

const MachineStorePage = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [beverageList, setBeverageList] = useState([]);

  const [coins, setCoins] = useState(0);
  const [text, setText] = useState("");
  const insertCoinHandler = (coin) => {
    axios
      .put("http://localhost:8000/", { coin })
      .then((response) => response.headers)
      .then(
        (data) => setCoins(data["x-coins"]),
        (error) => console.log(error)
      );
  };
  const retrieveCoins = () => {
    axios
      .delete("http://localhost:8000/")
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

    fetch("http://localhost:8000/inventory/")
      .then((response) => response.json())
      .then(
        (data) => setBeverageList(data),
        (error) => console.log(error)
      );

    console.log("beverageList", beverageList);
    setIsLoading(false);
  }, []);

  return (
    <>
      {!isLoading && (
        <>
          <BeverageList items={beverageList} setCoins={setCoins} />
          <div>Current credit: {coins} quarter coins</div>
          <div>{text}</div>
          <button onClick={() => insertCoinHandler(1)}>
            Insert Quarter Coin
          </button>
          <button onClick={() => retrieveCoins()}>Get Coins</button>
        </>
      )}
    </>
  );
};

export default MachineStorePage;
