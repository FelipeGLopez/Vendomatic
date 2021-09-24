import { useState, useEffect } from "react";
import React from "react";
import BeverageList from "../components/BeverageList";
import InsertionButton from "../components/InsertionButton";
import DeletionButton from "../components/DeletionButton";
import Text from "../components/Text";
import { axiosInstance } from "../utils/axiosInstance";

const Vendomatic = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [beverages, setBeverages] = useState([]);
  const [coins, setCoins] = useState(0);
  const [text, setText] = useState("Welcome!");

  const getInventory = () => {
    axiosInstance
      .get("/inventory/")
      .then((response) => response.data)
      .then(
        (data) => setBeverages(data),
        (error) => console.log(error)
      );
  };
  const getQuarterQuantity = () => {
    axiosInstance
      .get("/")
      .then((response) => response.data)
      .then(
        (data) => setCoins(data.quantity),
        (error) => console.log(error)
      );
  };

  useEffect(() => {
    getQuarterQuantity();
  }, []);

  useEffect(() => {
    setIsLoading(true);
    getInventory();
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
          <Text coins={coins} text={text} />
          <InsertionButton setCoins={setCoins} />
          <DeletionButton setCoins={setCoins} setText={setText} />
        </>
      )}
    </>
  );
};

export default Vendomatic;
