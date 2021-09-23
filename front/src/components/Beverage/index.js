import React from "react";

const BeverageList = (items) => {
  return (
    items.length >= 0 && (
      <>
        {items.map((item) => {
          return (
            <>
              <div>{item.id}</div>
              <div>{item.name}</div>
              <div>{item.value}</div>
              <div>{item.quantity}</div>
            </>
          );
        })}
      </>
    )
  );
};

export default BeverageList;
