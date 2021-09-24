import React from "react";
import { axiosInstance } from "../../utils/axiosInstance";
import Beverage from "../Beverage";

const BeverageList = (props) => {
  const { items, setCoins, setText } = props;

  const buyItem = (id, name) => {
    axiosInstance.put(`/inventory/${id}/`).then(
      (response) => {
        setCoins(response.headers["x-coins"]);
        setText(`You bought ${response.data.quantity} ${name}!`);
      },
      (error) => {
        if (error.response.status === 404) {
          setText(
            `You have ${error.response.headers["x-coins"]} coins!\nThere are no ${name} beverages left!`
          );
        } else if (error.response.status === 400) {
          setText(`You have ${error.response.headers["x-coins"]} coins!`);
        } else {
          console.log(error);
        }
      }
    );
  };

  return (
    items.length >= 0 && (
      <div className="row">
        {items.map((item) => {
          return <Beverage item={item} buyItem={buyItem} />;
        })}
      </div>
    )
  );
};

export default BeverageList;
