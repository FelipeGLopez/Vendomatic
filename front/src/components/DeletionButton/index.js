import React from "react";
import { axiosInstance } from "../../utils/axiosInstance";

const DeletionButton = (props) => {
  const { setCoins, setText } = props;

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

  return (
    <button className="btn btn-dark" onClick={() => retrieveCoins()}>
      Get Coins
    </button>
  );
};

export default DeletionButton;
