import React from "react";
import Beverage from "../Beverage";

const BeverageList = (props) => {
  const { items, setCoins, setText } = props;

  return (
    items.length >= 0 && (
      <div className="row">
        {items.map((item) => {
          return <Beverage item={item} setCoins={setCoins} setText={setText} />;
        })}
      </div>
    )
  );
};

export default BeverageList;
