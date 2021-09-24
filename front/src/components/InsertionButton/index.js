import React from "react";
import { axiosInstance } from "../../utils/axiosInstance";

const InsertionButton = (props) => {
  const { setCoins } = props;

  const insertCoinHandler = (coin) => {
    axiosInstance
      .put("/", { coin })
      .then((response) => response.headers)
      .then(
        (data) => setCoins(data["x-coins"]),
        (error) => console.log(error)
      );
  };

  return (
    <button
      className="btn btn-success"
      style={{ margin: "2%" }}
      onClick={() => insertCoinHandler(1)}
    >
      Insert Quarter Coin
    </button>
  );
};

export default InsertionButton;
